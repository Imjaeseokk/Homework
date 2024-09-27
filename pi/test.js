
var selectNum = 0;
// const Pi = Math.PI.toString().slice(2);
const Pi = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
var count = 0;


var btn = document.getElementsByClassName("number");
for(var i=0;i<btn.length;i++){
    btn[i].addEventListener("click",function(event){
        var value = this.innerText;

        if (value == Pi[count]){
            count++;
            result = "Success";
            document.getElementById('head').innerHTML = "Go to Pi";
        }
        else{
            value = 0;
            count = 0;
            result = "Fail";
            document.getElementById('head').innerHTML = "retry";
        }
        document.getElementById('count').innerHTML = count;
        document.getElementById('selectNum').innerHTML = value;
        document.getElementById('result').innerHTML = result;
    })
}
