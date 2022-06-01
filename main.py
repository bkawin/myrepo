from google.cloud import asset_v1
def export_tasks(request):
    client = asset_v1.AssetServiceClient()
    output_config = asset_v1.OutputConfig()
    output_config.bigquery_destination.dataset = "projects/tidal-triumph-348408/datasets/assets"
    output_config.bigquery_destination.table = "table"
    output_config.bigquery_destination.force = True
    request = asset_v1.ExportAssetsRequest(
        parent = "projects/tidal-triumph-348408",
        content_type = "RESOURCE",
        asset_types = [
            "logging.googleapis.com/LogBucket"
        ],
        output_config = output_config,
    )
    operation = client.export_assets(request=request)
    response = operation.result()
    return "Success", 200
