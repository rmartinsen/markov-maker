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

function createConvo() {
	var url = "/convo";

    fetch(url).then(function(response) {
        return response.json();
    }).then(function(json) {
        var formattedTest = conversationToHTML(json);
        $("#generated-text").html(formattedText);
    })
}

function createSentence() {
	var person = $("#person-select").val();
	var url = "/sentence/" + person;
    fetch(url).then(function(response) {
        return response.json();
    }).then(function(json) {
        var formattedText = sentenceToHTML(json);
        $("#generated-text").html(formattedText);
    })
    
}
