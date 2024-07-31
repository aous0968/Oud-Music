const bodyStyle = document.body.style;
let dark_colors = ["#313131", "#111", "white"];
let light_colors = ["#bdbdbd", "#fff", "black"];

if (localStorage.getItem('lightDarkMode') == 'light') {
    changeColors(bodyStyle, light_colors);
    changeLogo('light');
} else {
    changeColors(bodyStyle, dark_colors);
    changeLogo('dark');
}


$('#light_dark_mode_toggle').click(function (e) {
    if (localStorage.getItem('lightDarkMode') == 'light') {
        changeColors(bodyStyle, dark_colors);
        changeLogo('dark');
        localStorage.setItem('lightDarkMode', 'dark');
    } else {
        changeColors(bodyStyle, light_colors);
        changeLogo('light');
        localStorage.setItem('lightDarkMode', 'light');
    }

});

function changeColors(bodyStyle, colors) {
    for (let i = 0; i < colors.length; i++) {
        bodyStyle.setProperty(`--color${i + 1}`, colors[i]);
    }

}
function changeLogo(mode) {
    if (mode == "light") {
        $('#logo_black').show();
        document.getElementById('logo_black').style.opacity = 1;
        $('#logo_white').hide();
        document.getElementById('logo_white').style.opacity = 0;
    }
    else {
        $('#logo_white').show();
        document.getElementById('logo_white').style.opacity = 1;
        $('#logo_black').hide();
        document.getElementById('logo_black').style.opacity = 0;
    }
}