// wait until page loads
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

        .then(res => res.json())

        .then(data => {

            console.log(data); 

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
            "<p style='color:red;'>Error generating script</p>";
        });

    });

});


// copy
function copyScript(){
    let text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text);
    alert("Copied!");
}

// download
function downloadScript(){
    let text = document.getElementById("output").innerText;

    let blob = new Blob([text], { type: "text/plain" });
    let link = document.createElement("a");

    link.href = URL.createObjectURL(blob);
    link.download = "script.txt";

    link.click();
}