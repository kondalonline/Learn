import os
import functions_framework
from googleapiclient.discovery import build
from datetime import datetime

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def trigger_dataflow_on_gcs_change(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    outbucket = os.environ.get('OUTPUT_BUCKET')
    outfile =  os.environ.get('OUTPUT_FILE')
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]    

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")
    print(f"output_bucket: {outbucket}")
    print(f"output file: {outfile}")

    # Check if the event is for a new file creation
    if event_type != "google.cloud.storage.object.v1.finalized":
        print("Ignoring non-creation event")
        return

    # Extract date folder from file path
    file_path_parts = name.split("/")
    if len(file_path_parts) < 2:  # Check if file is in a subfolder
        print("Ignoring file not in a date folder")
        return
    date_folder = file_path_parts[0]

    # Check if date folder matches today's date
    today = datetime.now().strftime("%m%d%Y")
    if date_folder != today:
        print(f"Ignoring file in wrong date folder: {date_folder}")
        return

    # Set up Dataflow client
    dataflow = build('dataflow', 'v1b3')

    # Specify job details
    project_id = 'hellosam-282b3'
    template_path = 'gs://dataflow-templates-us-west1/latest/Word_Count' 
    job_name = 'triggered-job-from-gcs-' + timeCreated.replace(":", "-") 
    parameters = {
        'inputFile': f'gs://{bucket}/{name}',  # Pass the uploaded file path as a parameter
        'output': f'gs://{outbucket}/{outfile}',
        # Add other parameters as needed based on your Dataflow template
    }


    # Launch the Dataflow job
    request = dataflow.projects().templates().launch(
        projectId=project_id,
        gcsPath=template_path,
        body={
            'jobName': job_name,
            'parameters': parameters
        }
    )
    response = request.execute()

    print(f"Launched Dataflow job: {response['job']['id']}")
