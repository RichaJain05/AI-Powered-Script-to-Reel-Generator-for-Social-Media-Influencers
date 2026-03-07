// when generate button is clicked
document.getElementById("generate").addEventListener("click", function(){

    // getting user idea
    let idea = document.getElementById("idea").value;

    // if user does not enter idea
    if(idea === ""){
        alert("Please enter your reel idea first");
        return;
    }

    
    // show loading text
    document.getElementById("output").innerHTML = "Generating reel plan...";

    // small delay to simulate processing
    setTimeout(function(){

        // simple sample output
        let result = `
        <h3>Reel Plan</h3>

        <p><b>Hook:</b> Start the reel with a question to grab attention.</p>

        <p><b>Scene 1:</b> Introduce the topic briefly.</p>

        <p><b>Scene 2:</b> Explain the main idea or tip.</p>

        <p><b>Scene 3:</b> Give a quick example or advice.</p>

        <p><b>Caption:</b> ${idea} - Try this today!</p>

        <p><b>Hashtags:</b> #reelideas #contentcreator #socialmedia</p>
        `;

        // showing output on screen
         document.getElementById("output").innerHTML = result;
    }, 1500);

});