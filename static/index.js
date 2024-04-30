function isElementVisible(el) {
    let rect     = el.getBoundingClientRect(),
        vWidth   = window.innerWidth || document.documentElement.clientWidth,
        vHeight  = window.innerHeight || document.documentElement.clientHeight,
        efp      = function (x, y) { return document.elementFromPoint(x, y) };

    // Return false if it's not in the viewport
    if (rect.right < 0 || rect.bottom < 0
            || rect.left > vWidth || rect.top > vHeight)
        return false;

    // Return true if any of its four corners are visible
    return (
          el.contains(efp(rect.left,  rect.top))
      ||  el.contains(efp(rect.right, rect.top))
      ||  el.contains(efp(rect.right, rect.bottom))
      ||  el.contains(efp(rect.left,  rect.bottom))
    );
}

let fadeInDetect = document.getElementsByClassName('fadeIn-detect')[0];

const fadeIn = () =>{
    const elems = document.getElementsByClassName('fadein');
    elems[0].style.animation = 'fadeIn 0.4s forwards';
    elems[1].style.animation = 'fadeIn 0.4s forwards';
    elems[2].style.animation = 'fadeIn 0.4s forwards';
    elems[3].style.animation = 'fadeIn 0.4s forwards';
}

window.onscroll = function(e){
    if (isElementVisible(fadeInDetect)){
       setTimeout(fadeIn, 500);
    }
}