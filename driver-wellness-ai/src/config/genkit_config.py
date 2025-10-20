from genkit import GenKit

# Initialize GenKit with your API key
genkit_client = GenKit(api_key='YOUR_GENKIT_API_KEY')

# Configure default parameters
DEFAULT_PARAMS = {
    'project_id': 'driver_wellness',
    'environment': 'production'
}

def send_alert(alert_data):
    try:
        return genkit_client.send_alert(
            alert_type='drowsiness_detected',
            severity='high',
            data=alert_data,
            **DEFAULT_PARAMS
        )
    except Exception as e:
        print(f"Failed to send GenKit alert: {e}")
        return None
