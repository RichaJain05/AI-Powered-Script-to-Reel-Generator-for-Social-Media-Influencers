function generateScript(){

    let topic = document.getElementById("topic").value;
    let platform = document.getElementById("platform").value;
    let tone = document.getElementById("tone").value;
    let duration = document.getElementById("duration").value;
    let persona = document.getElementById("persona").value;

    if(topic === ""){
        alert("Please enter a topic first");
        return;
    }

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

    .then(response => response.json())

    .then(data => {

        let result = `
        <h2>Reel Script</h2>

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

        <hr>

        <h3>Reel Details</h3>

        <p><b>Platform:</b> ${data.platform}</p>
        <p><b>Tone:</b> ${data.tone}</p>
        <p><b>Duration:</b> ${data.duration} seconds</p>
        <p><b>Creator Persona:</b> ${data.persona}</p>
        `;

        document.getElementById("output").innerHTML = result;

    })

    .catch(error => {

        document.getElementById("output").innerHTML =
        "<p style='color:red;'>Error generating script.</p>";

        console.error(error);
    });

}