// when generate button is clicked
document.getElementById("generate").addEventListener("click", function(){

    // getting user idea
    let idea = document.getElementById("idea").value;

    // if user does not enter idea
    if(idea === ""){
        alert("Please enter your reel idea first");
        return;
    }

    // simple sample output
    let result = `
    <h3>Reel Plan</h3>

    <p><b>Hook:</b> Start the video with an interesting question.</p>

    <p><b>Scene 1:</b> Introduce the topic.</p>

    <p><b>Scene 2:</b> Explain the main point.</p>

    <p><b>Scene 3:</b> Give quick tip or example.</p>

    <p><b>Caption:</b> ${idea} - Try this today!</p>

    <p><b>Hashtags:</b> #reelideas #contentcreator #socialmedia</p>
    `;

    // showing output on screen
    document.getElementById("output").innerHTML = result;

});