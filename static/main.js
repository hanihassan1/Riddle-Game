$("#incorrect").on("click", function() {
    // $(".prog-result").html("");
    $('#incorrect').trigger('focus')
    $("ul").html("");
    $("#progress").addClass("hide");
    totaLtime = 0;
});

function save_name(){
    username = $("#name").val();
    localStorage.setItem("username", username)
}


























// function req_data(answers) {
//   var xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       document.getElementById("answer").innerHTML = this.responseText;
//       myResponse = JSON.parse(this.responseText);
//         if ((myResponse.results) == True) {
//     }
//     else {
//       return false
//     }
//   };
//   xhttp.open("GET", "{{url_for('get_question') }}" + "?question=" + "answers" + answers  , true);
//   xhttp.send();
// }
// }


// $("#answerId").on("click", function() {

//     req_data($("#answer_box").val());

// });
