
// Object for dropdown menu options
var monthObject = {
  "January": 31, "February":  29, "March": 31, "April" : 30, "May" : 31, "June" : 30,
  "July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31
}
window.onload = function() {
  var monthSel = document.getElementById("month");
  var daySel = document.getElementById("day");
  var submitButton = document.getElementById("submit-button");
  
  // Establish subject dropdown menu
  for (var x in monthObject) {
    monthSel.options[monthSel.options.length] = new Option(x, x);
  }
  monthSel.onchange = function() {
    daySel.length = 1; // Reset day options to base
    // console.log('Month Value: ',monthSel.value)
    if (!(submitButton.hasAttribute('disabled'))) { // If submit button is not disabled
      submitButton.setAttribute("disabled","");
    }

    // Display correct days per month
    var daysinMonth = monthObject[monthSel.value];
    for (let i = 1; i <= daysinMonth; i++) {
      daySel.options[i] = new Option(i, i)
    }
  }

  // When daySel change
  daySel.onchange = function () {
    // console.log('Month Selected: ', monthSel.value, '| Day Selected: ', daySel.value);
    // On day selection, check if month and day are not empty strings
    if (daySel.value != "") {
      submitButton.removeAttribute('disabled');
    }
  }
}