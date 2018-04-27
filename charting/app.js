

var data;
console.log('123here');
var table = d3.select("#data-table");
var tbody = d3.select("tbody").html("");
	
d3.json("data.js", function(error, data) {
	if (error) return console.warn(error);

	console.log(data);
	//for (var i = 0; i < data.length; i++) {
	for (var i = 0; i < 10; i++) {
		 var obj = data[i];
		 var row = tbody.append("tr").classed("table-row", true);
		 for (var key in obj) {
			 
			console.log("key=" + key + " " + obj[key]);
			row.append("td").html(obj[key]).classed("text-center", true).attr("data-th", key);
	  
		 }
	} 
});