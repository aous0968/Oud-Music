/* ///////////// */
/* ajax funciton */
/* ///////////// */

function ajaxReq_forValidation(
  req_type,
  req_url,
  req_datatype,
  success_function,
  req_div,
  req_id
) {
  let input_val = $(req_id).val();
  $.ajax({
    type: req_type,
    url: req_url,
    data: `req_data=${input_val}`,
    dataType: req_datatype,
    success: function (response) {
      success_function(response, req_div);
    },
  });
}

var success = function (response, req_div) {
  req_div.innerHTML = response["massage"];
  username_validation_div.classList.add("username-unique");
  if (response["good"]) {
    req_div.classList.remove("not");
  } else {
    req_div.classList.add("not");
  }
}
/* ///////// */
/* ///////// */
/* ///////// */






let req_divs = {
  username: ["fa-solid", "fa-signature"],
  first_name: ["fa-solid", "fa-user"],
  last_name: ["fa-regular", "fa-user"],
  email: ["fa-solid", "fa-at"],
  password: ["fa-solid", "fa-lock"],
  confirm_password: ["fa-regular", "fa-square-check"],
};

for (const [key, val] of Object.entries(req_divs)) {
  let req_div = document.getElementById(String(key))
  let icon = document.createElement('i')
  for (cls of val) {
    icon.classList.add(cls)
  }
  icon.classList.add('auth-icon')
  req_div.append(icon)
}


const username_validation_div = document.createElement("div");
document.getElementById('user name').append(username_validation_div);

$("#id_username").on(' blur keyup keydown', function (e) {
  ajaxReq_forValidation("POST", "username-unique/", "json", success, username_validation_div, "#id_username");
});

