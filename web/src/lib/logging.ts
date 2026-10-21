const LOGGING_INSTANCE_ID = import.meta.env.LOGGING_INSTANCE_ID;
const LOGGING_API_KEY = import.meta.env.SECRET_LOGGING_API_KEY;
const LOGGING_URL = import.meta.env.LOGGING_URL;

const authPair = `${LOGGING_INSTANCE_ID}:${LOGGING_API_KEY}`;
const encoded = Buffer.from(authPair).toString('base64');

const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Basic ${encoded}`,
};

const logger = (stringValue: string) => {
    const body = {
        resourceLogs: [{
            resource: {
                attributes: [
                    { key: "service.name", value: { stringValue: `ctf-${import.meta.env.MODE}` } }
                ]
            },
            scopeLogs: [{
                logRecords: [{
                    timeUnixNano: String(Date.now() * 1e6),
                    body: { stringValue }
                }]
            }]
        }]
    };

    fetch(LOGGING_URL, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(body)
    })
    .then(response => {
        console.log("status:", response.status);
        return response.text();
    })
    .then(data => console.log("body:", data))
    .catch(error => console.error("error:", error));
}

export default logger;