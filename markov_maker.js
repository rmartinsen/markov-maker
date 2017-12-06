function createConvo() {
	var url = "/convo";
	var result = $.get(url);

	var lines = "";

	result.done(function(data) {
		lines = data.map(function(line) {
			var return_str = "<strong>";
			return_str += line.name + "</strong>: ";
			return_str += line.sentence;
			return_str += "<br>";
			return return_str;
		})

		$("#generated-text").html(lines);
	})

	result.fail(function(){
		createConvo();
	})
}

function createSentence() {
	var person = $("#person-select").val();
	var url = "/sentence/" + person;
	var result = $.get(url);

	result.done(function(data){
		$("#generated-text").html(data);
	})

	result.fail(function(data){
		createSentence();
	})



}