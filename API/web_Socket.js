const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    console.log(`Received: ${message}`);
    // Send a response to the client
    ws.send(`You said: ${message}`);
  });
});



/*client */
/*const ws = new WebSocket('ws://localhost:8080');

ws.addEventListener('open', (event) => {
  ws.send('Hello, WebSocket!');
});

ws.addEventListener('message', (event) => {
  console.log(`Received: ${event.data}`);
});
 */