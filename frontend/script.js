// Generate Script Function (ONLY ONE FUNCTION)
function generateScript(event){

    // stop page refresh
    if(event) event.preventDefault();

    let topic = document.getElementById("topic").value;
    let platform = document.getElementById("platform").value;
    let tone = document.getElementById("tone").value;
    let duration = document.getElementById("duration").value;
    let persona = document.getElementById("persona").value;

    // validation
    if(topic.trim() === ""){
        alert("Please enter a topic first");
        return;
    }

    // loading
    document.getElementById("output").innerHTML = "<p>Generating script...</p>";

    fetch("http://127.0.0.1:8000/generate-reel", {
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

    .then(response => {
        if(!response.ok){
            throw new Error("Server error");
        }
        return response.json();
    })

    .then(data => {

        console.log("API:", data);

        let result = `
        <div class="script-box">
            <h3>Hook</h3>
            <p>${data.hook}</p>
        </div>

        <div class="script-box">
            <h3>Body</h3>
            <p>${data.body}</p>
        </div>

        <div class="script-box">
            <h3>Call To Action</h3>
            <p>${data.cta}</p>
        </div>

        <div class="reel-details">
            <h3>Explanation</h3>
            <p><b>Topic:</b> ${data.explanation.topic_used}</p>
            <p><b>Tone:</b> ${data.explanation.tone_used}</p>
            <p><b>Platform:</b> ${data.explanation.platform_used}</p>
            <p>${data.explanation.message}</p>
        </div>
        `;

        document.getElementById("output").innerHTML = result;
        document.getElementById("actions").style.display = "block";
    })

    .catch(error => {
        console.error("Error:", error);
        document.getElementById("output").innerHTML =
        "<p style='color:red;'>Error generating script</p>";
    });
}


// Copy
function copyScript(){
    let text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text)
    .then(() => alert("Copied!"))
    .catch(() => alert("Copy failed"));
}


// Download
function downloadScript(){
    let text = document.getElementById("output").innerText;

    let blob = new Blob([text], { type: "text/plain" });

    let link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "reel_script.txt";

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}