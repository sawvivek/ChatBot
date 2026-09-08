async function askQuestion() {
    const questionInput = document.getElementById("question");
    const answerArea = document.getElementById("answer-area");

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    // Display user's question
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.innerHTML = `<strong>You:</strong> ${question}`;

    answerArea.appendChild(userMessage);

    // Clear input box
    questionInput.value = "";

    // Show thinking message
    const thinkingMessage = document.createElement("div");
    thinkingMessage.className = "bot-message";
    thinkingMessage.innerHTML = `<strong>Bot:</strong> Thinking...`;

    answerArea.appendChild(thinkingMessage);

    try {
        // Send question to Flask
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        // Replace thinking message with actual answer
        thinkingMessage.innerHTML =
            `<strong>Bot:</strong> ${data.answer}`;

    } catch (error) {
        thinkingMessage.innerHTML =
            `<strong>Bot:</strong> Sorry, something went wrong.`;
    }
}


// Press Enter to send question
document.getElementById("question").addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        askQuestion();
    }

});