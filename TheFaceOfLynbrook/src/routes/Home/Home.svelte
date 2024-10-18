<svelte:head>
<title>The Face of Lynbrook</title>
</svelte:head>
<script>
	import { Link } from "svelte-navigator";
	import {state} from "../../stores/store.js"
	$state = "/"
	
</script>


<center>
<h1>The Face of Lynbrook</h1>
<h2>This is what a typical Lynbrook student looks like:</h2>

<div class="img_group">
<img src="imgs/home/lynbr_avg.png" alt="avg" width="200" height="200"/>
</div>

<h2>This is what the least typical Lynbrook students look like:</h2>

<div class="img_group">
<img src="imgs/home/lynbr_l3sd.png" alt="l3sd" width="200" height="200"/>
<img src="imgs/home/lynbr_r3sd.png" alt="r3sd" width="200" height="200"/>
</div>

<h2>This is what randomly generated Lynbrook students look like:</h2>

<div class="img_group">
	<img src="imgs/home/gen1.png" alt="gen1" width="200" height="200"/>
	<img src="imgs/home/gen2.png" alt="gen2" width="200" height="200"/>
</div>

<h3>Contribute <Link to="submit">here</Link>.</h3>
</center>



<style>
	.web_group{
		text-align: center;
	}
	.img_group{
		justify-content: right;
		display: block;
	}	

	h2{
		width: fit-content;
		margin-top: 30px;
		color: #ff3e00;
		font-size: 1.5em;
		font-weight: 100;
		outline: none;

	}

	h3{
		width: fit-content;
		margin-top: 30px;
		color: #ff3e00;
		font-size: 1em;
		font-weight: 100;
		outline: none;
	}

	img{
		margin:15px;
		transition: transform .2s;
		margin-top: 15px;
		border: 2px solid black;
	}

	img:hover {
  		transform: scale(1.2); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
	}
</style>
