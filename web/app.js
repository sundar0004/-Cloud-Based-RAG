const askBtn = document.getElementById("askBtn");
const queryEl = document.getElementById("query");
const modeEl = document.getElementById("mode");
const topkEl = document.getElementById("topk");
const answerEl = document.getElementById("answer");
const latencyEl = document.getElementById("latency");
const retrievedEl = document.getElementById("retrieved");

async function ask() {
  const query = queryEl.value.trim();
  if (!query) {
    answerEl.textContent = "Please enter a question.";
    return;
  }

  askBtn.disabled = true;
  askBtn.textContent = "Running...";

  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query,
        mode: modeEl.value,
        top_k: Number(topkEl.value),
      }),
    });

    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || "Request failed");
    }

    answerEl.textContent = data.answer;
    latencyEl.textContent = `Mode: ${data.mode} | Latency: ${data.latency_ms.toFixed(2)} ms`;

    if (!data.retrieved || data.retrieved.length === 0) {
      retrievedEl.textContent = "No chunks retrieved.";
    } else {
      retrievedEl.innerHTML = data.retrieved
        .map(
          (c) =>
            `<article class="chunk"><div class="src">${c.source} | score=${c.score.toFixed(4)}</div><div>${c.text}</div></article>`
        )
        .join("");
    }
  } catch (err) {
    answerEl.textContent = `Error: ${err.message}`;
    latencyEl.textContent = "";
    retrievedEl.textContent = "";
  } finally {
    askBtn.disabled = false;
    askBtn.textContent = "Ask";
  }
}

askBtn.addEventListener("click", ask);
queryEl.value = "What is retrieval-augmented generation?";
window.addEventListener("load", () => {
  setTimeout(() => {
    ask();
  }, 400);
});
