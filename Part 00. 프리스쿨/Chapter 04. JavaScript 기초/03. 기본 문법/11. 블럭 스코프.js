/**
 * Block Scope (블럭 스코프)
 * - 변수 유효 범위
 * - 내부에서 외부로 접근 가능
 * - 외부에서 내부로는 접근 X
 *
 * 처음부터 => var => 함수 단위 유효 범위
 * ES2015+ => let, const => 블럭 단위 유효 범위
 */

var globalVal = '전역 변수';
var varVal = '함수-단위';
const constVal = '블럭-단위';

for (let index = 0; index < 3; index++) {}

function outerFunc() {
	console.log(globalVal);
	console.log(innerVal);

	function innerFunc() {
		var innerVal = '함수 내부 지역 변수';
		console.log(globalVal);
		console.log(index);
	}
	innerFunc();

	return num;
}

{
	let a = 'a';
}

if (true) {
	var b = 'b';
	let a = 'a';
}

console.log(b);
console.log(a);
