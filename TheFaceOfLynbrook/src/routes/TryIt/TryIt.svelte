<script>
	import {state, genImgFile, justGenerated, lastGenerated, ganCallInProgress} from "../../stores/store.js"
	import { Circle } from 'svelte-loading-spinners';
	//import { createLoadObserver } from './util.js'
	$state = "/tryit"

	const  LOADING_IMG = "gens/loading.png"
	let isGanInProgress = false; 

	let src = $genImgFile;

	function imgDateVar(){
		// this is for readbility 
		// later: pull return out of ifelse, remove else.
		if($justGenerated){
			$lastGenerated = Date.now();
			$justGenerated = false; 
			return "?t=" + $lastGenerated
		} else {
			return "?t=" + $lastGenerated
		}
	}

	// const onloadGen = createLoadObserver(() => {
	// 	if(!$ganCallInProgress){
	// 		$ganCallInProgress = false; 
	// 		$justGenerated = true; 
	// 	}
	// })

	async function genImg() { 
		if(!$ganCallInProgress){
			$genImgFile = LOADING_IMG;
			var loadImage = new Image();
			loadImage.src = LOADING_IMG;
			$ganCallInProgress = true;
			loadImage.onload = function(){ 
				let [ganCallInProgressTemp, justGeneratedTemp] = [false, true];
				fetch("./generate")
					.then(d => d.text())
					.then(d => ([$genImgFile, ganCallInProgressTemp, justGeneratedTemp]  = [JSON.parse(d).imgFile, JSON.parse(d).success, !JSON.parse(d).success])) // inrpog = false
					$ganCallInProgress = false; 
					$justGenerated = true; 

 			}
		}
  	}
	function spinnerClass(){
		return $ganCallInProgress ? "spinner" : "";
	}

	function size(){
		return $ganCallInProgress ? 30 : 0;
	}
</script>

<h1>Try It Out!</h1>

<div class="imgContainer">
<!-- img provides absolute height / width dims - change this! -->

{#key $ganCallInProgress}
<!-- <img use:onloadGen class={ganCallInProgress==true ? "img_gen" : "img_def"} src={$genImgFile+ imgDateVar()} alt="Generation" height=256 width=256  /> -->
<img class={ganCallInProgress==true ? "img_gen" : "img_def"} src={$genImgFile + imgDateVar()} alt="Generation" height=256 width=256  />
<div class={spinnerClass()}>
<Circle size={size()}  color="#FF3E00" unit="px" duration="1s" />
</div>
{/key}
</div>

<center>
<button class="genButton" on:click={genImg}>Generate!</button>
</center>

<style>

	.imgContainer{
		position: relative;

	}

	.img_def{
		border: 2px solid black;
		transition: transform .2s; /* Animation */
	}

	.img_gen{
		opacity: 100%;
		background-color: rgb(255,255,255);
		border: 2px solid black;
		transition: transform .2s; /* Animation */
	}

	img:hover {
  		transform: scale(1.2); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
	}

	.spinner{
		position: absolute;
		left: 0;
		top: 0; 

		/*
		top:50%;
		left:50%; */
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 1;
	}

	.genButton{
		background-color: #ff3e00;
		border: none;
		color: lightblue;
		padding: 20px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 24px;
		font-weight: 100;
		margin: 25px 2px;
		border-radius: 32px;

	}
	.genButton:hover{
		background-color: #ff784b;
	}
	.genButton:active{
		background-color: rgb(253, 184, 184)	}
</style>
