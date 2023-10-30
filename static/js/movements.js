// define x and y html elements 
var x_element = document.getElementById('x');
var y_element = document.getElementById('y');

// define x and y 
let x = 0;
let y = 0;

// my object
var obj = document.getElementById('obj');

// movement elements
var top = document.getElementById('top');
var down = document.getElementById('down');
var left = document.getElementById('left');
var right = document.getElementById('right');



document.querySelectorAll('.btns button').forEach( btn =>{



  
    btn.addEventListener('click',()=>{
        
        if (btn.id == 'down'){
            y++
        }

        else if ( btn.id == 'top'){
            y--
        }
        
        else if ( btn.id == 'left'){
            x--
        }

        else if (btn.id == 'right') {
            x++
        }



        x_element.value = x;
        y_element.value = y;

        obj.style.top = y + 'px' ;
        obj.style.left = x + 'px';

    })
    

})
