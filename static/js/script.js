
// Object for dropdown menu options
var monthObject = {
    "January": 31, "February":  29, "March": 31, "April" : 30, "May" : 31, "June" : 30,
    "July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31
  }

// On load, create drop down menu for navbar
  window.onload = function() {
    var monthSel = document.getElementById("month");
    var daySel = document.getElementById("day");
    
    // Create month menu objects dropdown menu
    for (var x in monthObject) {
      monthSel.options[monthSel.options.length] = new Option(x, x);
    }
    monthSel.onchange = function() {
      daySel.length = 1; // Reset day options to base
  
      // Display correct days per month
      var daysinMonth = monthObject[monthSel.value];
      console.log(daysinMonth);
      for (let i = 1; i <= daysinMonth; i++) {
        daySel.options[i] = new Option(i, i)
      }
    }
}