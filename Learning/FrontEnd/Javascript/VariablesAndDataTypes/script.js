// *********************************** VARIABLES ******************************* //
// VAR LET CONST
// DECLAIRATION AND INITALIZATION

// var a = 12;
//-> WINDOWS MAIN ADD HOTA HAI.
//->FUNCTIONS SCOPED HOTA HAI.
//->APP FIRSE DECLARE KR SKTE HO SAME NAME SE AND ERROR NHI AYEGA.

// *****************************---------->>>>>>>>>>>>>>>>>>
// let a = 12;
// a = 13;
// console.log(a)
//-> Let ma value agar ma variable ma store krdi too uss same variabe ko re declare nhi kr skte matlab ki agar let a = 12 krdiya or next line ma phirse let a = 12 krdiya too terminal ma error dikhaega.
//-> Let variable secure rahata ha as compare to var beacuse ap esma ek name ka same variable nhi bana skte.
//-> agar hum let ma variable ki value change krna cahate ha voo hoo skti ha jase ki
//-> let a = 12 ya likha phir hum cahate ha ki a = 13 hoo jae too hoo skta ha error nhi ayega.

// ***********************---------------->>>>>>>>>>>>>>>>
// SCOPE (GLOBAL, BLOCK, FUCNTIONAL)
// ->GLOBAL SCOPE :- eska matlab ha ap esko kahi bhi access krskte hoo.
// ->BLOCK SCOPE :- eska matlab ha ki kahi bhi {} curly braces lag jae uska aandar access ho skta ha.
// ->FUNCTIONAL SCOPE :- eska matlab ha ki function ka aandar use hota ha.

// ************************----------------->>>>>>>>>>>>>>>
// TEMPORAL DEAD ZONE
// ESKA MATLAB HOTA HA PRINT PHALA KARA RAHE HO OR DECLARE BAD MA KR RAHE HO.
//EXAMPLE:-
// console.log(name) // THIS GIVE YOU AN ERROR
// let name = "ansh"

// ************************----------------->>>>>>>>>>>>>>>>>
// HOSTING IMPACT PER TYPE'
// HOSTING -> ek variable ko jab js mein banate hai to wo variable do hisso main toot jata hai or uska ek part upar chala jata hai or dusra part nicha initialization mai chala jata hai 

// var a = 12;


// PRACTISE QUESTION
//QUES-1 
// console.log(name)
// var name = "ansh"

//QUES-2
// console.log(a)
// let a = 12

//QUES-3
// var b = 12

// {
//     var b = 13
// }
// console.log(b)

//QUES-4
// let a = 10
// {
//     let a = 20
//     console.log("Inside : ", a)
// }
// console.log("Outside : ", a)


// ************************COMMON COFUSION QUESTION**********************
// Confusion 1:-
// if (true) {
//     var a = 1
//     let b = 2 // They snow an error because let is respect to block scope and var only respect functional block
// }
// console.log(a)
// console.log(b)

// Confusion 2:-
// const person = {name : "ansh"};
// person.name = "sharma";
// console.log(person)
// person = {};
// console.log(person)

// ******************************** DATA TYPES ********************************* // 
// TWO TYPES OF DATA TYPE IN JAVASCRIPT
// PRIMITVE AND REFERENCE 
// PRIMITIVE -> AISI SARI VALUE JINKO COPY KARNE PAR TUMHE EK REAL COPY MIL JAYE.
// EXAMPLE -> STRING, INT, CHAR, BOOLEAN, NULL, NUMBER, UNDEFINED, BIGINT.

// REFERENCE -> INKO COPY KARNE PAR REAL COPY NAHI MILEGI BUT APKO REFERENCE MILEGAA PARENTS KA.
// ARRAYS, OBJECTS, FUNCTION.

// [] -> array esma banta hai.
// {} -> object esma banta hai.
// () -> function esma banta hai.


// null ka matlab hai apne jaan boojh kar koi value nhi di
// undefind ka matlab ki aapne ek variable banya aur usey value nahi di to jo value mili voo by default value mili hai.
// NULL hum khud sa dete hai or undefined humko milti ha


// symbol -> unique immutable value

