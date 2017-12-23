function sentenceToHTML(json) {
    var html = "<li><strong>";
    html += json.name + "</strong>:"
    html += json.sentence;
    html += "</li>";
    return html;
}

function conversationToHTML(json) {
    html = "<ul>";
    html += json.map(function(line){
        return sentenceToHTML(line);
    });
    html += "</ul>";
    return html;
}

function setGeneratedText(text) {
    $("#generated-text").html(text);
}

function createConvo() {
	var url = "/convo";

    fetch(url).then(function(response) {
        return response.json();
    }).then(function(json) {
        var formattedText = conversationToHTML(json);
        setGeneratedText(formattedText);
    })
}

function createSentence() {
	var person = $("#person-select").val();
	var url = "/sentence/" + person;

    var response = fetch(url).then(function(response) {
        if (!response.ok) {
            throw Error(response.statusText);
        }
        return response.json();
    }).catch(function(response) {
        setGeneratedText("Error in creating text. Please try again.")
    })
                
    response.then(function(json) {
        var formattedText = sentenceToHTML(json);
        setGeneratedText(formattedText);
    })
    
}
