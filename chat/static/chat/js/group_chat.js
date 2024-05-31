// DOM elements
const messageInput = document.getElementById("chat-message-input");
const messageSubmit = document.getElementById("chat-message-submit");
const chatLog = document.getElementById("chat-log");

// Function format time
function formatTime(date) {
  let hours = date.getHours();
  let minutes = date.getMinutes();
  const ampm = hours >= 12 ? "pm" : "am";
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? "0" + minutes : minutes;
  const strTime = hours + ":" + minutes + " " + ampm;
  return strTime;
}

// Function send message
function sendMessage() {
  const message = messageInput.value.trim();
  if (message !== "") {
    // Create elements for username, message, and timestamp
    const messageBlock = document.createElement("div");
    messageBlock.classList.add("message-block");

    const usernameElement = document.createElement("p");
    usernameElement.textContent = currentUsername;
    usernameElement.style.fontWeight = "bold";

    const messageContainer = document.createElement("div");
    messageContainer.style.display = "flex";
    messageContainer.style.justifyContent = "space-between";
    messageContainer.style.alignItems = "center";
    messageContainer.style.marginBottom = "10px";

    const messageElement = document.createElement("p");
    messageElement.textContent = message;

    const timestampElement = document.createElement("p");
    timestampElement.textContent = formatTime(new Date());
    timestampElement.style.fontSize = "0.8em";
    timestampElement.style.color = "gray";

    // Append message and timestamp to the message container
    messageContainer.appendChild(messageElement);
    messageContainer.appendChild(timestampElement);

    // Append username and message container to the message block
    messageBlock.appendChild(usernameElement);
    messageBlock.appendChild(messageContainer);

    // Append message block to chat log
    chatLog.appendChild(messageBlock);

    // Clear message input
    messageInput.value = "";

    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
  }
}

messageSubmit.addEventListener("click", () => {
  sendMessage();
});

messageInput.addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    sendMessage();
  }
});

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + groupId + "/"
);

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  document.querySelector(
    "#chat-log"
  ).innerHTML += `<div>${data.user}: ${data.message}</div>`;
};

document.querySelector("#chat-message-submit").onclick = function (e) {
  const messageInputDom = document.querySelector("#chat-message-input");
  const message = messageInputDom.value;
  chatSocket.send(
    JSON.stringify({
      message: message,
    })
  );
  messageInputDom.value = "";
};
