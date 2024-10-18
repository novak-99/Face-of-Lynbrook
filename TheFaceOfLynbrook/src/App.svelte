
<script>
	import { Router, Route, Link, createHistory, createMemorySource} from "svelte-navigator";
	import Header from './Header.svelte';
	import BehindTheScenes from "./routes/BehindTheScenes/BehindTheScenes.svelte";
	import Submit from "./routes/Submit/Submit.svelte";
	import createHashSource from "./hashHistory.js";
	import {state, genImgFile, success, ganCallInProgress} from "./stores/store.js"
	import Tabs from "./shared/Tabs.svelte"
  	import Home from "./routes/Home/Home.svelte";
  	import TryIt from "./routes/TryIt/TryIt.svelte";

  	$genImgFile = "gens/def.jpg"
	$ganCallInProgress = false; 
	let rand = -1
</script>

<Router>

<main>

{#key ($state)}
 <Header/> 
 {/key}

	<Route path="/">
		{#key ($state)}
		<Home />
		{/key}
	</Route>

	{#key $success}
	<Route path="tryit">
		<TryIt />
	</Route>
	{/key}

	<Route path="behindthescenes">
		<BehindTheScenes/>
	</Route>

	<Route path="submit">
		<Submit />
	</Route>
</main>
</Router>


<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
