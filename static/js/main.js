function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function setError(msg) {
  document.getElementById("dot").className = "status-dot error";
  document.getElementById("result-body").innerHTML =
    `<span class="error-text">❌ ${escapeHtml(msg)}</span>`;
  document.getElementById("btn").disabled = false;
}

function setLoading() {
  document.getElementById("dot").className = "status-dot active";
  document.getElementById("source-bar").classList.remove("show");
  document.getElementById("result-body").innerHTML = `
    <div class="loading-wrap">
      <div class="spinner"></div>
      <span class="loading-text">크롤링 및 요약 중...</span>
    </div>`;
}

function setResult(summary, url) {
  document.getElementById("dot").className = "status-dot done";
  document.getElementById("result-body").innerHTML =
    `<p class="summary-text">${escapeHtml(summary)}</p>`;

  const sourceLink = document.getElementById("source-link");
  sourceLink.href = url;
  sourceLink.textContent = url;
  document.getElementById("source-bar").classList.add("show");
}

async function summarize() {
  const url = document.getElementById("url").value.trim();
  const btn = document.getElementById("btn");

  if (!url) {
    setError("URL을 입력해주세요");
    return;
  }

  btn.disabled = true;
  setLoading();

  try {
    const res = await fetch("/api/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url }),
    });

    const data = await res.json();

    if (!res.ok) {
      setError(data.detail || "알 수 없는 오류");
      return;
    }

    setResult(data.summary, url);

  } catch (err) {
    setError("서버에 연결할 수 없습니다");
  } finally {
    btn.disabled = false;
  }
}

// Enter 키 바인딩
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("url").addEventListener("keydown", (e) => {
    if (e.key === "Enter") summarize();
  });
});