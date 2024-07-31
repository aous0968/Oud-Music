  /* ///////////// */
 /* Adding icons  */
/* ///////////// */

let user_icon = document.createElement("i");
user_icon.classList.add("fa-solid", "fa-user", "auth-icon");
let user = document.getElementById("username");
user.append(user_icon);

let pass_icon = document.createElement("i");
pass_icon.classList.add("fa-solid", "fa-lock", "auth-icon");
let password = document.getElementById("password");
password.append(pass_icon);


  /* ///////////////////////////////////// */
 /* AJAX REQUEST for user name validation */
/* ///////////////////////////////////// */

// const username_validation_div = document.createElement("div");
// $("#Username").append(username_validation_div);


// function ajaxReq_forValidation(
//   req_type,
//   req_url,
//   req_datatype,
//   success_function,
//   req_div,
//   req_id
// ) {
//    console.log("request is good");
//    let input_val = $(req_id).val();
//   $.ajax({
//     type: req_type,
//     url: req_url,
//     data: `req_data=${input_val}`,
//     dataType: req_datatype,
//     success: function (response){
//       success_function(response , req_div);
//     },
//   });
// }

// var success = function (response, req_div) {
//   console.log(req_div);
//   console.log(response);
//   req_div.innerHTML = response["massage"];
//   if (response["good"]) {
//     if (!req_div.classList.replace("alert-danger", "alert-success")) {
//       req_div.classList.add("alert-success" , "alert");
//     }
//   } else {
//     if (!req_div.classList.replace("alert-success", "alert-danger")) {
//       req_div.classList.add("alert-danger" , "alert");
//     }
//   }
// }


// $("#id_username").on(' blur keyup keydown' , function(e){
//    ajaxReq_forValidation("POST","username-validation/","json",success,username_validation_div,"#id_username");
// });

/* /////////////// */