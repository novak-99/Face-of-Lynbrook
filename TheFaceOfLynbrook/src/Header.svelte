<svelte:head>
<title>{headers_dict[selected]}</title>
<link rel="icon" href="/imgs/header/logo.png">
</svelte:head>
<script>
	import {state} from "./stores/store.js"
	import Tabs from "./shared/Tabs.svelte"
  	import { useLocation } from "svelte-navigator";

	let storeLocale = useLocation()
	// convert obj to STR. 
	let currentLocale = JSON.stringify($storeLocale.pathname) 

	// tabs 
    // home, submit data, behind the scenes (ml explanation)
	let items = [["/", "Home"], ["/tryit", "Try It"], ["/submit", "Submit Data"], ["/behindthescenes", "Behind The Scenes"]];
	let headers = [["/", "The Face of Lynbrook"], ["/tryit", "Try It"], ["/submit", "Submit Data"], ["/behindthescenes", "Behind The Scenes"]];

	//https://stackoverflow.com/questions/52655148/convert-2d-array-to-object-using-map-or-reduce-in-javascript
	//js map fxn
	const headers_dict = Object.fromEntries(headers.map(([k, v]) => [k, v]));


	let selected = $state
	const changeSelected = (e) => {
		selected = e.detail
		//$state = selected

		// storeLocale = useLocation()
		// currentLocale = JSON.stringify($storeLocale.pathname) 
	}
</script>
<header>
	<Tabs {items} {selected} on:changeSelected={changeSelected}/>

		
</header>