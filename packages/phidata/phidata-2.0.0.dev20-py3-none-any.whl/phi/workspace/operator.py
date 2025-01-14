from pathlib import Path
from typing import Optional, Dict, List

import typer

from phi.api.workspace import log_workspace_event
from phi.cli.config import PhiCliConfig
from phi.cli.console import (
    print_heading,
    print_info,
    print_subheading,
    log_config_not_available_msg,
)
from phi.infra.enums import InfraType
from phi.infra.resource.group import InfraResourceGroup
from phi.api.schemas.workspace import (
    WorkspaceSchema,
    WorkspaceCreate,
    WorkspaceUpdate,
    WorkspaceEvent,
    UpdatePrimaryWorkspace,
)
from phi.workspace.config import WorkspaceConfig
from phi.workspace.enums import WorkspaceStarterTemplate
from phi.utils.log import logger

TEMPLATE_TO_NAME_MAP: Dict[WorkspaceStarterTemplate, str] = {
    WorkspaceStarterTemplate.api_app: "api-app",
    WorkspaceStarterTemplate.llm_app: "llm-app",
    WorkspaceStarterTemplate.django_app: "django-app",
    WorkspaceStarterTemplate.streamlit_app: "streamlit-app",
    WorkspaceStarterTemplate.data_platform: "data-platform",
    WorkspaceStarterTemplate.spark_data_platform: "spark-data-platform",
    WorkspaceStarterTemplate.snowflake_data_platform: "snowflake-data-platform",
}
TEMPLATE_TO_REPO_MAP: Dict[WorkspaceStarterTemplate, str] = {
    WorkspaceStarterTemplate.api_app: "https://github.com/phihq/api-app.git",
    WorkspaceStarterTemplate.llm_app: "https://github.com/phihq/llm-app.git",
    WorkspaceStarterTemplate.django_app: "https://github.com/phihq/django-app.git",
    WorkspaceStarterTemplate.streamlit_app: "https://github.com/phihq/streamlit-app.git",
    WorkspaceStarterTemplate.data_platform: "https://github.com/phihq/data-platform.git",
    WorkspaceStarterTemplate.spark_data_platform: "https://github.com/phihq/spark-data-platform.git",
    WorkspaceStarterTemplate.snowflake_data_platform: "https://github.com/phihq/snowflake-data-platform.git",
}


def create_workspace(name: Optional[str] = None, template: Optional[str] = None, url: Optional[str] = None) -> None:
    """Creates a new workspace.

    This function clones a template or url on the users machine at the path:
        cwd/name
    """
    import git
    from shutil import copytree
    from rich.prompt import Prompt

    from phi.cli.operator import initialize_phi
    from phi.utils.common import str_to_int
    from phi.utils.filesystem import rmdir_recursive
    from phi.workspace.helpers import get_workspace_dir_path
    from phi.utils.git import GitCloneProgress

    current_dir: Path = Path(".").resolve()

    # Phi should be initialized before creating a workspace
    phi_config: Optional[PhiCliConfig] = PhiCliConfig.from_saved_config()
    if not phi_config:
        init_success = initialize_phi()
        if not init_success:
            from phi.cli.console import log_phi_init_failed_msg

            log_phi_init_failed_msg()
            return
        phi_config = PhiCliConfig.from_saved_config()
        # If phi_config is still None, throw an error
        if not phi_config:
            log_config_not_available_msg()
            return

    ws_dir_name: Optional[str] = name
    repo_to_clone: Optional[str] = url
    ws_template = WorkspaceStarterTemplate.api_app
    templates = list(WorkspaceStarterTemplate.__members__.values())

    if repo_to_clone is None:
        # Get repo_to_clone from template
        if template is None:
            # Get starter template from the user if template is not provided
            # Display available starter templates and ask user to select one
            print_info("Select starter template or press Enter for default (api-app)")
            for template_id, template_name in enumerate(templates, start=1):
                print_info("  [{}] {}".format(template_id, template_name))

            # Get starter template from the user
            template_choices = [str(idx) for idx, _ in enumerate(templates, start=1)]
            template_inp_raw = Prompt.ask("Template Number", choices=template_choices, default="1", show_choices=False)
            # Convert input to int
            template_inp = str_to_int(template_inp_raw)

            if template_inp is not None:
                template_inp_idx = template_inp - 1
                ws_template = WorkspaceStarterTemplate[templates[template_inp_idx]]
            logger.debug("Selected: {}".format(ws_template.value))
        elif template.lower() in WorkspaceStarterTemplate.__members__.values():
            ws_template = WorkspaceStarterTemplate[template]
        else:
            raise Exception(f"{template} is not a supported template, please choose from: {templates}")
        repo_to_clone = TEMPLATE_TO_REPO_MAP.get(ws_template)

    if ws_dir_name is None:
        default_ws_name = "api-app"
        if url is not None:
            # Get default_ws_name from url
            default_ws_name = url.split("/")[-1].split(".")[0]
        else:
            # Get default_ws_name from template
            default_ws_name = TEMPLATE_TO_NAME_MAP.get(ws_template, "api-app")

        # Ask user for workspace name if not provided
        ws_dir_name = Prompt.ask("Workspace Name", default=default_ws_name)

    if ws_dir_name is None:
        logger.error("Workspace name is required")
        return
    if repo_to_clone is None:
        logger.error("URL or Template is required")
        return

    # Check if a workspace with the same name exists
    existing_ws_config: Optional[WorkspaceConfig] = phi_config.get_ws_config_by_dir_name(ws_dir_name)
    if existing_ws_config is not None:
        logger.error(f"Found existing record for a workspace at: {ws_dir_name}")
        delete_existing_ws_config = typer.confirm("Replace existing record?", default=True)
        if delete_existing_ws_config:
            phi_config.delete_ws(ws_dir_name)
        else:
            return

    # Check if we can create the workspace in the current dir
    ws_root_path: Path = current_dir.joinpath(ws_dir_name)
    if ws_root_path.exists():
        logger.error(f"Directory {ws_root_path} exists, please delete directory or choose another name for workspace")
        return

    print_info(f"Creating {str(ws_root_path)}")
    logger.debug("Cloning: {}".format(repo_to_clone))
    try:
        _cloned_git_repo: git.Repo = git.Repo.clone_from(
            repo_to_clone, str(ws_root_path), progress=GitCloneProgress()  # type: ignore
        )
    except Exception as e:
        logger.error(e)
        return

    # Remove existing .git folder
    _dot_git_folder = ws_root_path.joinpath(".git")
    _dot_git_exists = _dot_git_folder.exists()
    if _dot_git_exists:
        logger.debug(f"Deleting {_dot_git_folder}")
        try:
            _dot_git_exists = not rmdir_recursive(_dot_git_folder)
        except Exception as e:
            logger.warning(f"Failed to delete {_dot_git_folder}: {e}")
            logger.info("Please delete the .git folder manually")
            pass

    phi_config.add_new_ws_to_config(
        ws_dir_name=ws_dir_name,
        ws_root_path=ws_root_path,
    )

    try:
        # workspace_dir_path is the path to the ws_root/workspace dir
        workspace_dir_path: Path = get_workspace_dir_path(ws_root_path)
        workspace_secrets_dir = workspace_dir_path.joinpath("secrets").resolve()
        workspace_example_secrets_dir = workspace_dir_path.joinpath("example_secrets").resolve()

        print_info(f"Creating {str(workspace_secrets_dir)}")
        copytree(
            str(workspace_example_secrets_dir),
            str(workspace_secrets_dir),
        )
    except Exception as e:
        logger.warning(f"Could not create workspace/secrets: {e}")
        logger.warning("Please manually copy workspace/example_secrets to workspace/secrets")

    print_info(f"Your new workspace is available at {str(ws_root_path)}\n")
    setup_workspace(ws_root_path=ws_root_path)


def setup_workspace(ws_root_path: Path) -> None:
    """Setup a phi workspace at `ws_root_path`.

    1. Validate pre-requisites
    1.1 Check ws_root_path is available
    1.2 Check PhiCliConfig is available
    1.3 Validate WorkspaceConfig is available
    1.4 Load workspace and set as active
    1.5 Check if remote origin is available
    1.6 Create anon user if not available

    2. Create or Update WorkspaceSchema
    If a ws_schema exists for this workspace, this workspace has a record in the backend
    2.1 Create WorkspaceSchema for a NEWLY CREATED WORKSPACE
    2.2 Set workspace as primary if needed
    2.3 Update WorkspaceSchema if git_url has changed
    """
    from phi.cli.operator import initialize_phi
    from phi.utils.git import get_remote_origin_for_dir

    print_heading("Running workspace setup\n")

    ######################################################
    ## 1. Validate Pre-requisites
    ######################################################
    ######################################################
    # 1.1 Check ws_root_path is available
    ######################################################
    _ws_is_valid: bool = ws_root_path is not None and ws_root_path.exists() and ws_root_path.is_dir()
    if not _ws_is_valid:
        logger.error("Invalid directory: {}".format(ws_root_path))
        return

    ######################################################
    # 1.2 Check PhiCliConfig is available
    ######################################################
    phi_config: Optional[PhiCliConfig] = PhiCliConfig.from_saved_config()
    if not phi_config:
        # Phidata should be initialized before workspace setup
        init_success = initialize_phi()
        if not init_success:
            from phi.cli.console import log_phi_init_failed_msg

            log_phi_init_failed_msg()
            return
        phi_config = PhiCliConfig.from_saved_config()
        # If phi_config is still None, throw an error
        if not phi_config:
            raise Exception("Failed to initialize phi")

    ######################################################
    # 1.3 Validate WorkspaceConfig is available
    ######################################################
    logger.debug(f"Checking for a workspace at {ws_root_path}")
    ws_config: Optional[WorkspaceConfig] = phi_config.get_ws_config_by_path(ws_root_path)
    if ws_config is None:
        # This happens if
        # - The user is setting up a workspace not previously setup on this machine
        # - OR the user ran `phi init -r` which erases existing records of workspaces
        logger.debug(f"Could not find an existing workspace at path: {ws_root_path}")

        # In this case, the local workspace directory exists but PhiCliConfig does not have a record
        print_info(f"Adding {ws_root_path} as a workspace")
        phi_config.add_new_ws_to_config(
            ws_dir_name=ws_root_path.stem,
            ws_root_path=ws_root_path,
        )
        ws_config = phi_config.get_ws_config_by_path(ws_root_path)
    else:
        logger.debug(f"Found workspace at {ws_config.ws_dir_name}")

    # If the ws_config is still None it means the workspace is corrupt
    if ws_config is None:
        logger.error(f"Could not use workspace from: {ws_root_path}")
        logger.error("Please try again")
        return

    ######################################################
    # 1.4 Load workspace and set as active
    ######################################################
    # Load and save the workspace config
    ws_config.load()
    # Get the workspace dir name
    ws_dir_name = ws_config.ws_dir_name
    # Set the workspace as active if it is not already
    # update_primary_ws is a flag to update the primary workspace in the backend
    update_primary_ws = False
    if phi_config.active_ws_dir is None or phi_config.active_ws_dir != ws_dir_name:
        phi_config.active_ws_dir = ws_dir_name
        update_primary_ws = True

    ######################################################
    # 1.5 Check if remote origin is available
    ######################################################
    git_remote_origin_url: Optional[str] = get_remote_origin_for_dir(ws_root_path)
    logger.debug("Git origin: {}".format(git_remote_origin_url))

    ######################################################
    # 1.6 Create anon user if not logged in
    ######################################################
    if phi_config.user is None:
        from phi.api.user import create_anon_user

        logger.debug("Creating anon user")
        anon_user = create_anon_user()
        if anon_user is not None:
            phi_config.user = anon_user

    ######################################################
    ## 2. Create or Update WorkspaceSchema
    ######################################################
    # If a ws_schema exists for this workspace, this workspace is synced with the api
    ws_schema: Optional[WorkspaceSchema] = ws_config.ws_schema
    if phi_config.user is not None:
        ######################################################
        # 2.1 Create WorkspaceSchema for NEW WORKSPACE
        ######################################################
        if ws_schema is None or ws_schema.id_workspace is None:
            from phi.api.workspace import create_workspace_for_user
            from phi.workspace.helpers import generate_workspace_name

            # If ws_schema is None, this is a NEWLY CREATED WORKSPACE.
            # We make a call to the api to create a new ws_schema
            new_workspace_name = generate_workspace_name(ws_dir_name=ws_dir_name)
            logger.debug("Creating ws_schema for new workspace")
            logger.debug(f"ws_dir_name: {ws_dir_name}")
            logger.debug(f"workspace_name: {new_workspace_name}")

            ws_schema = create_workspace_for_user(
                user=phi_config.user,
                workspace=WorkspaceCreate(
                    ws_name=new_workspace_name,
                    git_url=git_remote_origin_url,
                    is_primary_for_user=True,
                ),
            )
            if ws_schema is not None:
                ws_config = phi_config.update_ws_config(ws_dir_name=ws_dir_name, ws_schema=ws_schema)
            else:
                logger.debug("Failed to sync workspace with api. Please setup again")

        ######################################################
        # 2.2 Set workspace as primary if needed
        ######################################################
        elif update_primary_ws:
            from phi.api.workspace import update_primary_workspace_for_user

            logger.debug("Setting workspace as primary")
            logger.debug(f"ws_dir_name: {ws_dir_name}")
            logger.debug(f"workspace_name: {ws_schema.ws_name}")

            updated_workspace_schema = update_primary_workspace_for_user(
                user=phi_config.user,
                workspace=UpdatePrimaryWorkspace(
                    id_workspace=ws_schema.id_workspace,
                    ws_name=ws_schema.ws_name,
                ),
            )

            if updated_workspace_schema is not None:
                # Update the ws_schema for this workspace.
                ws_config = phi_config.update_ws_config(ws_dir_name=ws_dir_name, ws_schema=updated_workspace_schema)
            else:
                logger.debug("Failed to sync workspace with api. Please setup again")

        ######################################################
        # 2.3 Update WorkspaceSchema if git_url has changed
        ######################################################
        if ws_schema is not None and ws_schema.git_url != git_remote_origin_url:
            from phi.api.workspace import update_workspace_for_user

            logger.debug("Updating git_url for existing workspace")
            logger.debug(f"ws_dir_name: {ws_dir_name}")
            logger.debug(f"workspace_name: {ws_schema.ws_name}")
            logger.debug(f"Existing git_url: {ws_schema.git_url}")
            logger.debug(f"New git_url: {git_remote_origin_url}")

            updated_workspace_schema = update_workspace_for_user(
                user=phi_config.user,
                workspace=WorkspaceUpdate(
                    id_workspace=ws_schema.id_workspace,
                    git_url=git_remote_origin_url,
                ),
            )
            if updated_workspace_schema is not None:
                # Update the ws_schema for this workspace.
                ws_config = phi_config.update_ws_config(ws_dir_name=ws_dir_name, ws_schema=updated_workspace_schema)
            else:
                logger.debug("Failed to sync workspace with api. Please setup again")

    if ws_config is not None:
        # logger.debug("Workspace Config: {}".format(ws_config.model_dump_json(indent=2)))
        print_subheading("Setup complete! Next steps:")
        print_info("1. Start workspace:")
        print_info("\tphi ws up")
        print_info("2. Stop workspace:")
        print_info("\tphi ws down")
        if ws_config.workspace_settings is not None:
            scripts_dir = ws_config.workspace_settings.scripts_dir
            install_ws_file = f"sh {ws_root_path}/{scripts_dir}/install.sh"
            print_info("3. Install workspace dependencies:")
            print_info(f"\t{install_ws_file}")

        if ws_config.ws_schema is not None and phi_config.user is not None:
            log_workspace_event(
                user=phi_config.user,
                workspace_event=WorkspaceEvent(
                    id_workspace=ws_config.ws_schema.id_workspace,
                    event_type="setup",
                    event_status="success",
                    event_data={"workspace_root_path": str(ws_root_path)},
                ),
            )
    else:
        print_info("Workspace setup unsuccessful. Please try again.")

    ######################################################
    ## End Workspace setup
    ######################################################


def start_workspace(
    phi_config: PhiCliConfig,
    ws_config: WorkspaceConfig,
    target_env: Optional[str] = None,
    target_infra: Optional[InfraType] = None,
    target_group: Optional[str] = None,
    target_name: Optional[str] = None,
    target_type: Optional[str] = None,
    dry_run: Optional[bool] = False,
    auto_confirm: Optional[bool] = False,
    force: Optional[bool] = None,
) -> None:
    """Start a Phi Workspace. This is called from `phi ws up`"""
    if ws_config is None:
        logger.error("WorkspaceConfig invalid")
        return
    if ws_config.workspace_settings is None:
        logger.error("WorkspaceSettings invalid")
        return

    # Set the local environment variables before processing configs
    ws_config.set_local_env()

    # Get resource groups to deploy
    resource_groups_to_create: List[InfraResourceGroup] = ws_config.get_resource_groups(
        env=target_env,
        infra=target_infra,
        order="create",
    )
    num_rgs_to_create = len(resource_groups_to_create)
    num_rgs_created = 0
    num_resources_created = 0

    if num_rgs_to_create == 0:
        print_info("No resources to create")
        return

    logger.debug(f"Deploying {num_rgs_to_create} resource groups")
    for rg in resource_groups_to_create:
        num_resources_created += rg.create_resources(
            group_filter=target_group,
            name_filter=target_name,
            type_filter=target_type,
            dry_run=dry_run,
            auto_confirm=auto_confirm,
            force=force,
            workspace_settings=ws_config.workspace_settings,
        )
        num_rgs_created += 1
        # print white space between runs
        print_info("")
        logger.debug(f"Deployed {num_resources_created} resources in {num_rgs_created} resource groups")

    if dry_run:
        return

    if num_resources_created == 0:
        return

    print_info(f"# ResourceGroups deployed: {num_rgs_created}/{num_rgs_to_create}\n")

    workspace_event_status = "in_progress"
    if num_rgs_to_create == num_rgs_created:
        print_subheading("Workspace started")
        workspace_event_status = "success"
    else:
        logger.error("Workspace start failed")
        workspace_event_status = "failed"

    if phi_config.user is not None and ws_config.ws_schema is not None and ws_config.ws_schema.id_workspace is not None:
        # Log workspace start event
        log_workspace_event(
            user=phi_config.user,
            workspace_event=WorkspaceEvent(
                id_workspace=ws_config.ws_schema.id_workspace,
                event_type="start",
                event_status=workspace_event_status,
                event_data={
                    "target_env": target_env,
                    "target_infra": target_infra,
                    "target_group": target_group,
                    "target_name": target_name,
                    "target_type": target_type,
                    "dry_run": dry_run,
                    "auto_confirm": auto_confirm,
                    "force": force,
                },
            ),
        )


def stop_workspace(
    phi_config: PhiCliConfig,
    ws_config: WorkspaceConfig,
    target_env: Optional[str] = None,
    target_infra: Optional[InfraType] = None,
    target_group: Optional[str] = None,
    target_name: Optional[str] = None,
    target_type: Optional[str] = None,
    dry_run: Optional[bool] = False,
    auto_confirm: Optional[bool] = False,
    force: Optional[bool] = None,
) -> None:
    """Stop a Phi Workspace. This is called from `phi ws down`"""
    if ws_config is None:
        logger.error("WorkspaceConfig invalid")
        return
    if ws_config.workspace_settings is None:
        logger.error("WorkspaceSettings invalid")
        return

    # Set the local environment variables before processing configs
    ws_config.set_local_env()

    # Get resource groups to delete
    resource_groups_to_delete: List[InfraResourceGroup] = ws_config.get_resource_groups(
        env=target_env,
        infra=target_infra,
        order="delete",
    )
    num_rgs_to_delete = len(resource_groups_to_delete)
    num_rgs_deleted = 0
    num_resources_deleted = 0

    if num_rgs_to_delete == 0:
        print_info("No resources to delete")
        return

    logger.debug(f"Deleting {num_rgs_to_delete} resource groups")
    for rg in resource_groups_to_delete:
        num_resources_deleted += rg.delete_resources(
            group_filter=target_group,
            name_filter=target_name,
            type_filter=target_type,
            dry_run=dry_run,
            auto_confirm=auto_confirm,
            force=force,
            workspace_settings=ws_config.workspace_settings,
        )
        num_rgs_deleted += 1
        # print white space between runs
        print_info("")
        logger.debug(f"Deleted {num_resources_deleted} resources in {num_rgs_deleted} resource groups")

    if dry_run:
        return

    if num_resources_deleted == 0:
        return

    print_info(f"# ResourceGroups deleted: {num_rgs_deleted}/{num_rgs_to_delete}\n")

    workspace_event_status = "in_progress"
    if num_rgs_to_delete == num_rgs_deleted:
        print_subheading("Workspace stopped")
        workspace_event_status = "success"
    else:
        logger.error("Workspace stop failed")
        workspace_event_status = "failed"

    if phi_config.user is not None and ws_config.ws_schema is not None and ws_config.ws_schema.id_workspace is not None:
        # Log workspace stop event
        log_workspace_event(
            user=phi_config.user,
            workspace_event=WorkspaceEvent(
                id_workspace=ws_config.ws_schema.id_workspace,
                event_type="stop",
                event_status=workspace_event_status,
                event_data={
                    "target_env": target_env,
                    "target_infra": target_infra,
                    "target_group": target_group,
                    "target_name": target_name,
                    "target_type": target_type,
                    "dry_run": dry_run,
                    "auto_confirm": auto_confirm,
                    "force": force,
                },
            ),
        )


def update_workspace(
    phi_config: PhiCliConfig,
    ws_config: WorkspaceConfig,
    target_env: Optional[str] = None,
    target_infra: Optional[InfraType] = None,
    target_group: Optional[str] = None,
    target_name: Optional[str] = None,
    target_type: Optional[str] = None,
    dry_run: Optional[bool] = False,
    auto_confirm: Optional[bool] = False,
    force: Optional[bool] = None,
) -> None:
    """Update a Phi Workspace. This is called from `phi ws patch`"""
    if ws_config is None:
        logger.error("WorkspaceConfig invalid")
        return
    if ws_config.workspace_settings is None:
        logger.error("WorkspaceSettings invalid")
        return

    # Set the local environment variables before processing configs
    ws_config.set_local_env()

    # Get resource groups to update
    resource_groups_to_update: List[InfraResourceGroup] = ws_config.get_resource_groups(
        env=target_env,
        infra=target_infra,
        order="create",
    )
    num_rgs_to_update = len(resource_groups_to_update)
    num_rgs_updated = 0
    num_resources_updated = 0

    if num_rgs_to_update == 0:
        print_info("No resources to update")
        return

    logger.debug(f"Updating {num_rgs_to_update} resource groups")
    for rg in resource_groups_to_update:
        num_resources_updated += rg.update_resources(
            group_filter=target_group,
            name_filter=target_name,
            type_filter=target_type,
            dry_run=dry_run,
            auto_confirm=auto_confirm,
            force=force,
            workspace_settings=ws_config.workspace_settings,
        )
        num_rgs_updated += 1
        # print white space between runs
        print_info("")
        logger.debug(f"Updated {num_resources_updated} resources in {num_rgs_updated} resource groups")

    if dry_run:
        return

    if num_resources_updated == 0:
        return

    print_info(f"# ResourceGroups updated: {num_rgs_updated}/{num_rgs_to_update}\n")

    workspace_event_status = "in_progress"
    if num_rgs_to_update == num_rgs_updated:
        print_subheading("Workspace updated")
        workspace_event_status = "success"
    else:
        logger.error("Workspace update failed")
        workspace_event_status = "failed"

    if phi_config.user is not None and ws_config.ws_schema is not None and ws_config.ws_schema.id_workspace is not None:
        # Log workspace start event
        log_workspace_event(
            user=phi_config.user,
            workspace_event=WorkspaceEvent(
                id_workspace=ws_config.ws_schema.id_workspace,
                event_type="update",
                event_status=workspace_event_status,
                event_data={
                    "target_env": target_env,
                    "target_infra": target_infra,
                    "target_group": target_group,
                    "target_name": target_name,
                    "target_type": target_type,
                    "dry_run": dry_run,
                    "auto_confirm": auto_confirm,
                    "force": force,
                },
            ),
        )


def delete_workspace(phi_config: PhiCliConfig, ws_to_delete: Optional[List[str]]) -> None:
    if ws_to_delete is None or len(ws_to_delete) == 0:
        print_heading("No workspaces to delete")
        return

    for ws_dir in ws_to_delete:
        phi_config.delete_ws(ws_dir_name=ws_dir)


def set_workspace_as_active(ws_dir_name: Optional[str], load: bool = True) -> None:
    from phi.cli.operator import initialize_phi

    ######################################################
    ## 1. Validate Pre-requisites
    ######################################################
    ######################################################
    # 1.1 Check PhiConf is valid
    ######################################################
    phi_config: Optional[PhiCliConfig] = PhiCliConfig.from_saved_config()
    if not phi_config:
        # Phidata should be initialized before workspace setup
        init_success = initialize_phi()
        if not init_success:
            from phi.cli.console import log_phi_init_failed_msg

            log_phi_init_failed_msg()
            return
        phi_config = PhiCliConfig.from_saved_config()
        # If phi_config is still None, throw an error
        if not phi_config:
            raise Exception("Failed to initialize phi")

    ######################################################
    # 1.2 Check ws_root_path is valid
    ######################################################
    # By default, we assume this command is run from the workspace directory
    ws_root_path: Optional[Path] = None
    if ws_dir_name is None:
        # If the user does not provide a ws_name, that implies `phi set` is ran from
        # the workspace directory.
        ws_root_path = Path(".").resolve()
    else:
        # If the user provides a workspace name manually, we find the dir for that ws
        ws_root_path = phi_config.get_ws_root_path_by_dir_name(ws_dir_name)
        if ws_root_path is None:
            logger.error(f"Could not find workspace {ws_dir_name}")
            return

    ws_dir_is_valid: bool = ws_root_path is not None and ws_root_path.exists() and ws_root_path.is_dir()
    if not ws_dir_is_valid:
        logger.error("Invalid workspace directory: {}".format(ws_root_path))
        return

    ######################################################
    # 1.3 Validate PhiWsData is available i.e. a workspace is available at this directory
    ######################################################
    logger.debug(f"Checking for a workspace at path: {ws_root_path}")
    active_ws_config: Optional[WorkspaceConfig] = phi_config.get_ws_config_by_path(ws_root_path)
    if active_ws_config is None:
        # This happens when the workspace is not yet setup
        print_info(f"Could not find a workspace at path: {ws_root_path}")
        print_info("If this workspace has not been setup, please run `phi ws setup` from the workspace directory")
        return

    print_heading(f"Setting workspace {active_ws_config.ws_dir_name} as active")
    if load:
        try:
            active_ws_config.load()
        except Exception as e:
            logger.error("Could not load workspace config, please fix errors and try again")
            logger.error(e)
            return

    ######################################################
    # 1.4 Make api request if updating active workspace
    ######################################################
    logger.debug("Updating active workspace api")
    if phi_config.user is not None:
        ws_schema: Optional[WorkspaceSchema] = active_ws_config.ws_schema
        if ws_schema is None:
            logger.warning(f"Please setup {active_ws_config.ws_dir_name} by running `phi ws setup`")
        else:
            from phi.api.workspace import update_primary_workspace_for_user

            updated_workspace_schema = update_primary_workspace_for_user(
                user=phi_config.user,
                workspace=UpdatePrimaryWorkspace(
                    id_workspace=ws_schema.id_workspace,
                    ws_name=ws_schema.ws_name,
                ),
            )
            if updated_workspace_schema is not None:
                # Update the ws_schema for this workspace.
                phi_config.update_ws_config(
                    ws_dir_name=active_ws_config.ws_dir_name, ws_schema=updated_workspace_schema
                )

    ######################################################
    ## 2. Set workspace as active
    ######################################################
    phi_config.active_ws_dir = active_ws_config.ws_dir_name
    print_info("Active workspace updated")
    return
