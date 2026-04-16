// function runs when user clicks generate button
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

    document.getElementById("output").innerHTML = "Generating script...";

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
        <h3>Hook</h3>
        <p>${data.hook}</p>

        <h3>Body</h3>
        <p>${data.body}</p>

        <h3>Call To Action</h3>
        <p>${data.cta}</p>
        `;

        document.getElementById("output").innerHTML = result;

    })
    .catch(error => {
        document.getElementById("output").innerHTML = "Error generating script.";
        console.log(error);
    });

}
