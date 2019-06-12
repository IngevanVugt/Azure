<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/html">
<title>Champ data.nl</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz"
        crossorigin="anonymous">
<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.7.0/css/all.css' integrity='sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ' crossorigin='anonymous'>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-teal.css">


<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Raleway", sans-serif}
body, html {
    height: 100%;
    line-height: 1.8;
}
* {
    box-sizing: border-box;
}
.btn-liquid {
	display: inline-block;
	position: relative;
	width: 240px;
	height: 60px;
	border-radius: 27px;
	color: #fff;
	font: 700 14px/60px "Droid Sans", sans-serif;
	letter-spacing: 0.05em;
	text-align: center;
	text-decoration: none;
	text-transform: uppercase;
}
.btn-liquid .inner {
	position: relative;
	z-index: 2;
}
.btn-liquid canvas {
	position: absolute;
	top: -50px;
	right: -50px;
	bottom: -50px;
	left: -50px;
	z-index: 1;
}
#regForm {
  background-color: #ffffff;
  margin: 100px auto;
  font-family: Raleway;
  padding: 40px;
  width: 70%;
  min-width: 300px;
}
h1 {
  text-align: center;
}
input {
  padding: 10px;
  width: 100%;
  font-size: 17px;
  font-family: Raleway;
  border: 1px solid #aaaaaa;
}
/* Mark input boxes that gets an error on validation: */
input.invalid {
  background-color: #ffdddd;
}
/* Hide all steps by default: */
.tab {
  display: none;
}
button {
  background-color: #4CAF50;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  font-size: 17px;
  font-family: Raleway;
  cursor: pointer;
}
button:hover {
  opacity: 0.8;
}
#prevBtn {
  background-color: #bbbbbb;
}
/* Make circles that indicate the steps of the form: */
.step {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbbbbb;
  border: none;
  border-radius: 50%;
  display: inline-block;
  opacity: 0.5;
}
.step.active {
  opacity: 1;
}
/* Mark the steps that are finished and valid: */
.step.finish {
  background-color: #4CAF50;
}
/* Full height image header */
.bgimg-1 {
  background-position: center;
  background-size: cover;
  background-image: url("https://live.staticflickr.com/2816/33487168601_1ddff1f6c7_b.jpg");
  min-height: 100%;
}
.w3-bar .w3-button {
  padding: 16px;
}
    .container {
    max-width: 640px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 13px;
}
ul.ks-cboxtags {
    list-style: none;
    padding: 20px;
}
ul.ks-cboxtags li{
  display: inline;
}
ul.ks-cboxtags li label{
    display: inline-block;
    background-color: rgba(255, 255, 255, .9);
    border: 2px solid rgba(139, 139, 139, .3);
    color: #adadad;
    border-radius: 25px;
    white-space: nowrap;
    margin: 3px 0px;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    transition: all .2s;
}
ul.ks-cboxtags li label {
    padding: 8px 12px;
    cursor: pointer;
}
ul.ks-cboxtags li label::before {
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: 12px;
    padding: 2px 6px 2px 2px;
    content: "\f067";
    transition: transform .3s ease-in-out;
}
ul.ks-cboxtags li input[type="checkbox"]:checked + label::before {
    content: "\f00c";
    transform: rotate(-360deg);
    transition: transform .3s ease-in-out;
}
ul.ks-cboxtags li input[type="checkbox"]:checked + label {
    border: 2px solid #1bdbf8;
    background-color: #12bbd4;
    color: #fff;
    transition: all .2s;
}
ul.ks-cboxtags li input[type="checkbox"] {
  display: absolute;
}
ul.ks-cboxtags li input[type="checkbox"] {
  position: absolute;
  opacity: 0;
}
ul.ks-cboxtags li input[type="checkbox"]:focus + label {
  border: 2px solid #e9a1ff;
}
  .btn {
  background-color: teal; /* Blue background */
  border: none; /* Remove borders */
  color: white; /* White text */
  padding: 6px 5px; /* Some padding */
  font-size: 10px; /* Set a font size */
  cursor: pointer; /* Mouse pointer on hover */
}
/* Darker background on mouse-over */
.btn:hover {
  background-color: black;
}
</style>
<body>

<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-card" id="myNavbar">
    <img src="https://media1.tenor.com/images/ab51b48f52f991e82edbb4846794ad47/tenor.gif?itemid=12939685" CLASS="w3-circle w3-border w3-left" width="50px">
      <a href={{ url_for("home") }} class="w3-bar-item w3-button w3-wide w3-teal w3-opacity ">CHAMPY</a>
      <a href={{ url_for('protein') }} class="w3-bar-item w3-button">PROTEIN</a>
      <a href={{ url_for('organisms') }} class="w3-bar-item w3-button">ORGANISM</a>
      <a href={{ url_for('blast') }} class="w3-bar-item w3-button">BLAST</a>
     <div class="w3-right w3-hide-small">
      <a href="#about" class="w3-bar-item w3-button">ABOUT</a>
      <a href="#team" class="w3-bar-item w3-button"><i class="fa fa-group"></i> TEAM</a>

    </div>
      <button onclick="document.getElementById('id01').style.display='block'" class="w3-button w3-theme w3-opacity " style="width:100%">Click here to search Database</button>

    <!-- Right-sided navbar links -->

    <!-- Hide right-floated links on small screens and replace them with a menu icon -->

    <a href="javascript:void(0)" class="w3-bar-item w3-button w3-right w3-hide-large w3-hide-medium" onclick="w3_open()">
      <i class="fa fa-bars"></i>
    </a>
  </div>
</div>

<!-- Sidebar on small screens when clicking the menu icon -->
<nav class="w3-sidebar w3-bar-block w3-black w3-card w3-animate-left w3-hide-medium w3-hide-large" style="display:none" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button w3-large w3-padding-16">Close ×</a>
  <a href="#about" onclick="w3_close()" class="w3-bar-item w3-button">ABOUT</a>
  <a href="#team" onclick="w3_close()" class="w3-bar-item w3-button">TEAM</a>
  <a href={{ url_for('organisms') }} onclick="w3_close()" class="w3-bar-item w3-button">Organisme</a>
  <a href={{ url_for('protein') }} onclick="w3_close()" class="w3-bar-item w3-button">Eiwit</a>
</nav>

<!-- Header with full-height image -->
<header class="bgimg-1 w3-display-container w3-grayscale-min" id="home">
  <div class="w3-display-left w3-text-white " style="padding:48px">
    <span class="w3-jumbo w3-hide-small" style="-webkit-text-stroke: 1px black">Champ data</span><br>
    <span class="w3-xxlarge w3-hide-large w3-hide-medium">Champ data</span><br>
    <span class="w3-large w3-text-black" style="-webkit-text-stroke: 1px black">The database with all te info on micro organisms in compost researched with metagenomics</span>
  </div>
</header>


  <div id="id01" class="w3-modal">
    <div class="w3-modal-content">
        <span onclick="document.getElementById('id01').style.display='none'"
        class="w3-button w3-display-topright w3-red w3-text-white"><b>x</b></span>
      <div class="w3-container">
        <form action='/results' id="regForm"  method="post">
          <h1>Database search:</h1>
          <!-- One "tab" for each step in the form: -->
          <div class="tab w3-center">What do you want to see?
            <div class="w3-bar-block w3-container">
            <div class="container">
              <ul class="ks-cboxtags">
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxOne" name="checkboxOne" value="Blast_type"><label for="checkboxOne">Blast type</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxTwo"  name="checkboxTwo" value="Score" ><label for="checkboxTwo">score</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxThree"  name="checkboxThree" value="Query_cover" ><label for="checkboxThree">Query cover</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxFour" name="checkboxFour" value="E_value"><label for="checkboxFour">E-value</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxFive" name="checkboxFive" value="Percent_ident"><label for="checkboxFive">Percent identity</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxSix" name="checkboxSix" value="Accessiecode"><label for="checkboxSix">Accesiecode</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxSeven" name="checkboxSeven" value="Organisme"><label for="checkboxSeven">Organisme</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxEight" name="checkboxEight" value="Taxonomie"><label for="checkboxEight">Taxonomie</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxNine" name="checkboxNine" value="Read_type"><label for="checkboxNine">Read type</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxTen" name="checkboxTen" value="Header"><label for="checkboxTen">Header</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxEleven" name="checkboxEleven" value="Sequentie"><label for="checkboxEleven">Sequentie</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxTwelve" name="checkboxTwelve" value="Bio_domein"><label for="checkboxTwelve">Biologisch domein</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxThirteen" name="checkboxThirteen" value="Bio_proces"><label for="checkboxThirteen">Biologisch proces</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxFourteen" name="checkboxFourteen" value="Prot_locatie"><label for="checkboxFourteen">Locatie</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxFifteen" name="checkboxFifteen" value="Bio_functie"><label for="checkboxFifteen">Functie</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxSixteen" name="checkboxSixteen" value="Prot_naam"><label for="checkboxSixteen">Eiwit naam</label></li>
              </ul>
              </div>
            </div>
          </div>
          <div class="tab">Would you like to search an organism or protein?
            <p><input placeholder="Search organism..." oninput="this.className = ''" name="organisme" ></p>
            <p><input placeholder="Search Protein..." oninput="this.className = ''" name="eiwit" ></p>
          </div>
          <div class="tab">Some more detailed filter options:
            <div class="w3-row-padding" style="margin:8px -16px;">
          <div class="w3-half w3-margin-bottom">
              <select name="E_value_parameter">
                 <option value=">=">More</option>
                 <option value="=">Equal</option>
                 <option value="<=">Less</option>
              </select>
              <label>E-value</label>
            <input class="w3-input w3-border" oninput="this.className = ''" type="number" value="" name="E-value_value" min="0,000005" max="6">
          </div>
          <div class="w3-half">
            <select name="Score_parameter">
                 <option value=">=">More</option>
                 <option value="=">Equal</option>
                 <option value="<=">Less</option>
            </select>
              <label>Score</label>
                <input class="w3-input w3-border" oninput="this.className = ''" type="number" value="" name="Score_value" min="0" max="1000">
          </div>
        </div>
          <div class="w3-row-padding" style="margin:8px -16px;">
          <div class="w3-half w3-margin-bottom">
            <select name="percent_identity_parameter">
                 <option value=">=">More</option>
                 <option value="=">Equal</option>
                 <option value="<=">Less</option>
              </select>
              <label>Percent identity %</label>
            <input class="w3-input w3-border" oninput="this.className = ''" type="number" value="" name="Percent identity" min="0" max="100">
          </div>
          <div class="w3-half">
            <select name="query_cover_parameter">
                 <option value=">=">More</option>
                 <option value="=">Equal</option>
                 <option value="<=">Less</option>
              </select>
              <label>Query cover %</label>
          <input class="w3-input w3-border" oninput="this.className = ''" type="number" value="" name="Query cover" min="0" max="100">
          </div>

        </div>
          </div>
          <div class="tab">What kind of results do you want?
             <div class="w3-panel w3-wide w3-theme w3-opacity">
              <p >READS</p>
             </div>
              <div class="w3-container">
             <ul class="ks-cboxtags">
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxread1" name = "checkboxread1" value="1"><label for="checkboxread1">Read 1</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxread2" name = "checkboxread2" value="2"><label for="checkboxread2">Read 2</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxread3" name = "checkboxread3" value="(Read_type = 1 or Read_type = 2)"><label for="checkboxread3">Read 1 & 2</label></li>
             </ul>
          </div>
          <div class="w3-panel w3-wide w3-theme w3-opacity">
              <p >BLAST TYPE</p>
             </div>
              <ul class="ks-cboxtags">
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxblastx" name = "checkboxblastx" value="'blastx'"><label for="checkboxblastx">Blastx</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxtblastx" name = "checkboxtblastx" value="'tblastx'"><label for="checkboxtblastx">tBlastx</label></li>
                <li><input type="checkbox" oninput="this.className = ''" id="checkboxboth" name = "checkboxboth" value="(Blast_type = 'blastx' or Blast_type= 'tblastx')"><label for="checkboxboth">tBlastx & Blastx</label></li>
              </ul>

        </div>
          </div>
          <div style="overflow:auto;">
            <div style="float:right;">
              <button type="button" class="w3-theme" id="prevBtn" onclick="nextPrev(-1)">Previous</button>
              <button type="button" class="w3-theme" id="nextBtn" onclick="nextPrev(1)">Next</button>
            </div>
          </div>
  <!-- Circles which indicates the steps of the form: -->
          <div style="text-align:center;margin-top:40px;">
            <span class="step w3-theme-d2"></span>
            <span class="step w3-theme-d2"></span>
            <span class="step w3-theme-d2"></span>
            <span class="step w3-theme-d2"></span>
          </div>
        </form>
      </div>
    </div>
  </div>

  <div class="w3-display-bottomleft w3-text-grey w3-large" style="padding:24px 48px">
    <i class="fa fa-facebook-official w3-hover-opacity"></i>
    <i class="fa fa-instagram w3-hover-opacity"></i>
    <i class="fa fa-snapchat w3-hover-opacity"></i>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
  </div>


<!-- About Section -->
<div class="w3-container" style="padding:128px 16px" id="about">
  <h3 class="w3-center">ABOUT THIS DATABASE</h3>
  <p class="w3-center w3-large">Key features</p>
  <div class="w3-row-padding w3-center" style="margin-top:64px">
    <div class="w3-quarter">
      <i class="fa fa-desktop w3-margin-bottom w3-jumbo w3-center"></i>
      <p class="w3-large">Responsive</p>
      <p> This website and its database is responsive and so is usable on any device and browser</p>
    </div>
    <div class="w3-quarter">
      <i class="fa fa-heart w3-margin-bottom w3-jumbo"></i>
      <p class="w3-large">Passion</p>
      <p>The data has been accuired by a team of passionate scientist, wanting to help the farming industry</p>
    </div>
    <div class="w3-quarter">
      <i class="fa fa-diamond w3-margin-bottom w3-jumbo"></i>
      <p class="w3-large">Design</p>
      <p>The website is designed beautifully, with eye for the costumer and so is easily usable</p>
    </div>
    <div class="w3-quarter">
      <i class="fa fa-cog w3-margin-bottom w3-jumbo"></i>
      <p class="w3-large">Techinical specs</p>
      <p>Scoring matrix: Blossum 62 <br> E-value cut off: 10e^-5 <br> other filters: no multicelulair or ecoli<br> ...</p>
    </div>
  </div>
</div>
<hr>

<!-- Team Section -->
<div class="w3-container" style="padding:128px 16px" id="team">
  <h3 class="w3-center">THE TEAM</h3>
  <p class="w3-center w3-large">The ones who runs this company</p>
  <div class="w3-row-padding " style="margin-top:64px">
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card">
        <img src="https://media1.tenor.com/images/ca0b0adec83cda504850e3fe4293616c/tenor.gif?itemid=13655818" alt="Youri" style="width:100%">
        <div class="w3-container">
          <h3>Youri Geboers</h3>
          <p class="w3-opacity">The one who quit</p>
          <p>Not everyone makes it to the end<br> . </p>
          <p><button class="w3-button w3-theme w3-opacity w3-block"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card">
        <img src="https://media.giphy.com/media/1kTHYEtLiLB1wUBwCS/giphy.gif" alt="Inge" style="width:100%">
        <div class="w3-container">
          <h3>Inge van Vugt</h3>
          <p class="w3-opacity">Blast and query specialist</p>
          <p>To blast is to know. To query is to show<br><br> .</p>
          <p><button class="w3-button w3-theme w3-opacity w3-block"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card">
        <img src="https://media.giphy.com/media/7TcdtHOCxo3meUvPgj/giphy.gif" alt="Marnic" style="width:100%">
        <div class="w3-container">
          <h3>Marnick Verhulst </h3>
          <p class="w3-opacity">Database filler</p>
          <p>An empty database is a useless database<br>
           <br> .</p>
          <p><button class="w3-button w3-theme w3-opacity w3-block"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card">
        <img src="https://media.giphy.com/media/1rRs3lmXv86WDAF2sd/giphy.gif" alt="Sanne" style="width:100%">
        <div class="w3-container">
          <h3>Sanne van Staveren</h3>
          <p class="w3-opacity">Web Designer</p>
          <p>Design is to make something pleasantly usable and stunning. No compensation of one or the other</p>
          <p><button class="w3-button w3-theme w3-opacity w3-block"><i class="fa fa-envelope"></i> Contact</button></p>
        </div>
      </div>
    </div>
  </div>
</div>


<!-- Footer -->
<footer class="w3-center w3-black w3-padding-64">
  <a href="#home" class="w3-button w3-light-grey"><i class="fa fa-arrow-up w3-margin-right"></i>To the top</a>
  <div class="w3-xlarge w3-section">
    <i class="fa fa-facebook-official w3-hover-opacity"></i>
    <i class="fa fa-instagram w3-hover-opacity"></i>
    <i class="fa fa-snapchat w3-hover-opacity"></i>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
  </div>
  <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-text-green">w3.css</a></p>
</footer>
<script scr="https://codepen.io/waaark/pen/VbgwEM.js"></script>
<script>
// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}
// Toggle between showing and hiding the sidebar when clicking the menu icon
var mySidebar = document.getElementById("mySidebar");
function w3_open() {
  if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
  } else {
    mySidebar.style.display = 'block';
  }
}
// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
}
</script>
<script>
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab
function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}
function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}
function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}
function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}
</script>

</body>
</html>
