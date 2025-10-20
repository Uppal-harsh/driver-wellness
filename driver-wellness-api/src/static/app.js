document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const status = document.getElementById('status');
    const alertStatus = document.getElementById('alertStatus');
    
    let monitoring = false;
    let websocket = null;

    startBtn.addEventListener('click', () => {
        if (!monitoring) {
            startMonitoring();
        }
    });

    stopBtn.addEventListener('click', () => {
        if (monitoring) {
            stopMonitoring();
        }
    });

    function startMonitoring() {
        websocket = new WebSocket('ws://localhost:8765');
        
        websocket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            updateUI(data);
        };

        monitoring = true;
        status.textContent = 'Status: Monitoring';
    }

    function stopMonitoring() {
        if (websocket) {
            websocket.close();
        }
        monitoring = false;
        status.textContent = 'Status: Not Monitoring';
    }

    function updateUI(data) {
        if (data.is_drowsy) {
            alertStatus.textContent = 'ALERT: Drowsiness Detected!';
            alertStatus.style.color = 'red';
        } else {
            alertStatus.textContent = 'No Alerts';
            alertStatus.style.color = 'green';
        }
    }
});
