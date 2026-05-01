// 1. UPDATE THIS URL with your actual Render Backend URL
const API_BASE_URL = "https://your-backend-name.onrender.com"; 

let currentScriptText = "";

document.addEventListener("DOMContentLoaded", function(){
    const btn = document.getElementById("generateBtn");

    btn.addEventListener("click", function(e){
        e.preventDefault();

        let topic = document.getElementById("topic").value;
        let platform = document.getElementById("platform").value;
        let tone = document.getElementById("tone").value;
        let duration = document.getElementById("duration").value;
        let persona = document.getElementById("persona").value;

        if(topic.trim() === ""){
            alert("Please enter a topic first");
            return;
        }

        document.getElementById("output").innerHTML = "<p>Generating script...</p>";

        // 2. Updated to use API_BASE_URL
        fetch(`${API_BASE_URL}/generate-reel`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                topic: topic,
                platform: platform,
                tone: tone,
                duration: parseInt(duration),
                persona: persona
            })
        })
        .then(res => res.json())
        .then(data => {
            console.log(data); 
            currentScriptText = `${data.hook}\n\n${data.body}\n\n${data.cta}`;

            let html = `
            <div class="script-box">
                <h3>Hook</h3>
                <p>${data.hook}</p>
            </div>
            <div class="script-box">
                <h3>Body</h3>
                <p>${data.body}</p>
            </div>
            <div class="script-box">
                <h3>CTA</h3>
                <p>${data.cta}</p>
            </div>
            <div class="reel-details">
                <h3>Explanation</h3>
                <p>${data.explanation.message}</p>
            </div>
            `;

            document.getElementById("output").innerHTML = html;
            document.getElementById("actions").style.display = "block";
        })
        .catch(err => {
            console.error(err);
            document.getElementById("output").innerHTML =
            "<p style='color:red;'>Error generating script. Check if backend is awake.</p>";
        });
    });
});

// Generate video function
function generateVideo() {
    if (!currentScriptText) {
        alert("Please generate a script first!");
        return;
    }

    const btn = document.getElementById("generateVideoBtn");
    const originalText = btn.innerText;
    btn.innerText = "Generating Video (Processing on Cloud)...";
    btn.disabled = true;

    // 3. Updated to use API_BASE_URL and corrected 'script_content' field
    fetch(`${API_BASE_URL}/generate-video`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            script_content: currentScriptText // Changed from script_text to match backend
        })
    })
    .then(res => {
        if (!res.ok) throw new Error("Failed to generate video");
        return res.blob();
    })
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "ai_reel.mp4";
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
        alert("Video generated and downloaded!");
    })
    .catch(err => {
        console.error(err);
        alert("Error generating video. Make sure your Google API Key is set on Render.");
    })
    .finally(() => {
        btn.innerText = originalText;
        btn.disabled = false;
    });
}

// Utility functions
function copyScript(){
    let text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text);
    alert("Copied to clipboard!");
}

function downloadScript(){
    let text = document.getElementById("output").innerText;
    let blob = new Blob([text], { type: "text/plain" });
    let link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "script.txt";
    link.click();
}
