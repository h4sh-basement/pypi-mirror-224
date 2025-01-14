import typer
from pathlib import Path
from rich import print
from lumaCLI.models import Config, RequestInfo
from lumaCLI.utils import (
    json_to_dict,
    validate_json,
    get_config,
    send_config,
    send_request_info,
)
from lumaCLI.common import (
    LumaURL,
    DryRun,
    NoConfig,
    MetadataDir,
)

# Create Typer application
app = typer.Typer(no_args_is_help=True, pretty_exceptions_show_locals=False)


@app.command()
def ingest(
    metadata_dir: Path = MetadataDir,
    luma_url: str = LumaURL,
    dry_run: bool = DryRun,
    no_config: bool = NoConfig,
) -> RequestInfo:
    """
    Ingests a bundle of JSON files (manifest.json, catalog.json, sources.json, run_results.json) located in the specified directory to a Luma endpoint.
    If any of these files is not present in the directory, the command will fail. Uses the current working directory if 'metadata_dir' is not specified.
    """

    # get_config
    config: Config = get_config()
    should_send_config = not no_config

    # Define JSON paths
    manifest_json_path = metadata_dir / "manifest.json"
    catalog_json_path = metadata_dir / "catalog.json"
    sources_json_path = metadata_dir / "sources.json"
    run_results_json_path = metadata_dir / "run_results.json"

    # Validate each JSON file
    is_manifest_json_valid = validate_json(
        json_path=manifest_json_path, endswith="manifest.json"
    )
    is_catalog_json_valid = validate_json(
        json_path=catalog_json_path, endswith="catalog.json"
    )
    is_sources_json_valid = validate_json(
        json_path=sources_json_path, endswith="sources.json"
    )
    is_run_results_json_valid = validate_json(
        json_path=run_results_json_path, endswith="run_results.json"
    )

    # Ensure all JSON files are valid
    if not all(
        [
            is_manifest_json_valid,
            is_catalog_json_valid,
            is_sources_json_valid,
            is_run_results_json_valid,
        ]
    ):
        raise typer.Exit(1)

    # Convert each JSON to dict
    manifest_dict = json_to_dict(json_path=manifest_json_path)
    catalog_dict = json_to_dict(json_path=catalog_json_path)
    sources_dict = json_to_dict(json_path=sources_json_path)
    run_results_dict = json_to_dict(json_path=run_results_json_path)

    # Define bundle dict
    bundle_dict = {
        "manifest_json": manifest_dict,
        "catalog_json": catalog_dict,
        "sources_json": sources_dict,
        "run_results_json": run_results_dict,
    }

    # If in dry run mode, print the bundle and exit
    if dry_run:
        print(bundle_dict)
        raise typer.Exit(0)

    endpoint = f"{luma_url}/api/v1/dbt"

    # Create the request information
    request_info = RequestInfo(
        url=endpoint,
        method="POST",
        payload=bundle_dict,
        verify=False,
        timeout=(3.05, 60 * 30),
    )

    if config and should_send_config:
        config_response = send_config(config=config, luma_url=luma_url)

    response = send_request_info(request_info)
    if not response.ok:
        raise typer.Exit(1)

    return response


@app.command()
def send_test_results(
    metadata_dir: Path = MetadataDir,
    luma_url: str = LumaURL,
    dry_run: bool = DryRun,
    no_config: bool = NoConfig,
) -> RequestInfo:
    """
    Sends the 'run_results.json' file located in the specified directory to a Luma endpoint.
    The command will fail if the 'run_results.json' file is not present in the directory. The current working directory is used if 'metadata_dir' is not specified.
    """

    # get_config
    config: Config = get_config()
    should_send_config = not no_config

    # Define the path to 'run_results.json'
    run_results_path = Path(metadata_dir) / "run_results.json"

    # Validate 'run_results.json'
    is_run_results_json_valid = validate_json(run_results_path, "run_results.json")

    # Ensure 'run_results.json' is valid
    if not is_run_results_json_valid:
        print(f"[red]run_results.json not valid[/red]")
        raise typer.Exit(1)

    # Convert 'run_results.json' to dict
    run_results_dict = json_to_dict(json_path=run_results_path)

    # If in dry run mode, print the test results and exit
    if dry_run:
        print(run_results_dict)
        raise typer.Exit(0)

    endpoint = f"{luma_url}/api/v1/dbt/run_results"

    # Create and return the request information for test results
    request_info = RequestInfo(
        url=endpoint,
        method="POST",
        payload=run_results_dict,
        verify=False,
        timeout=(3.05, 60 * 30),
    )

    if config and should_send_config:
        config_response = send_config(config=config, luma_url=luma_url)

    response = send_request_info(request_info)
    if not response.ok:
        raise typer.Exit(1)
    return response


# Run the application
if __name__ == "__main__":
    app()
