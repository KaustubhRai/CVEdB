function capec_showMore() {  
  console.log('Random bullshit go')
  const btnText = document.getElementById("capec-Btn");
  const capecItemList = document.getElementById("capec-item-list");
  // SOLUTION 1 for READ MORE Button
  const isShowingCapecList = capecItemList.style.display !== "none";
  if (isShowingCapecList) {
    btnText.innerHTML = "Read More"
    capecItemList.style.display = "none"
  }
  if (!isShowingCapecList) {
    btnText.innerHTML = "Read Less"
    capecItemList.style.display = "inline"
  }
// SOLUTION 2 for READ MORE Button 
  
  // if (btnText.innerHTML === "Read More") { // showing all capec items
  //   capecItemList.style.display = "block"
  //   btnText.innerHTML = "Read Less"; 
  // } else {
  //   btnText.innerHTML = "Read More"; 
  //   capecItemList.style.display = "none"
  // }
}

