const quizData = [
    {
        question: ">>> a = 'wtf'\n>>> b = 'wtf'\n>>> a is b",
        options: ["True","False"],
        correctAnswer: 0
    },
    {
        question: ">>> a = 'wtf!'\n>>> b = 'wtf!'\n>>> a is b",
        options: ["True","False"],
        correctAnswer: 1
    },
    {
        question: ">>> (False == False) in [False]\nFalse\n>>> False == (False in [False])\nFalse\n>>> False == False in [False]",
        options: ["True","False"],
        correctAnswer: 0
    },
    {
        question: `>>> 1 > 0 < 1
                True
                >>> (1 > 0) < 1`,
        options: ["True","False"],
        correctAnswer: 1
    }
];

let currentQuestion = 0;
let correctAnswers = 0;

function loadQuestion(){
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');

    questionElement.innerHTML = quizData[currentQuestion].question.replace(/\n/g,'<br>');

    optionsElement.innerHTML = '';
    quizData[currentQuestion].options.forEach((option, index) =>{
        optionsElement.innerHTML += `<button onclick="checkAnswer(${index})">${option}</button><br>`;

        // ' <- single quote'
        // ` <- backtick: 백틱은 ES6(ECMAScript 2015)부터 도입된 템플릿 리터럴을 지원합니다. 템플릿 리터럴은 변수를 문자열 안에 직접 삽입하거나, 여러 줄의 문자열을 처리할 때 유용합니다.

    });
}

function updateQuizStatus(){
    document.getElementById('currentQuizNumber').textContent = currentQuestion;
    document.getElementById('currentAnswerCount').textContent = correctAnswers;
}


function checkAnswer(selectedIndex){
    if (selectedIndex == quizData[currentQuestion].correctAnswer){
        alert('correct!');
        correctAnswers++;
    } else {
        alert('wrong :(');
    }

    currentQuestion++;
    updateQuizStatus();
    if (currentQuestion < quizData.length){
        loadQuestion();
    } else {
        alert('The quiz is end. Press "Restart" to restart!');
    }

}

function restartQuiz(){
    currentQuestion = 0;
    correctAnswers = 0;
    
    updateQuizStatus();
    loadQuestion();

}


loadQuestion();



