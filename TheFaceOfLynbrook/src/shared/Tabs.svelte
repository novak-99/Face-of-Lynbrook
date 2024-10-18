<script>
    import { Link } from "svelte-navigator";
    import {createEventDispatcher} from 'svelte';
    const dispatch = createEventDispatcher();
    export let items; 
    export let selected;
</script>

<!-- <nav class="tabs">
    <ul>
    {#each items as item}
    <li on:click={() => dispatch('changeSelected', item)}>
        <Link to="/"><div class:active={item === selected}>{item}</div></Link></li>
    {/each}
    </ul>
</nav> -->

<nav class="tabs">
    <ul>
        {#each items as item}
            <!-- move this to style  -->
            <div class={item[0] === selected ? "active" : "inactive"}>
                <Link to="{item[0]}" style="text-decoration:none;"> 
                    <li on:click={() => dispatch('changeSelected', item[0])}>
                        <div class:active_inside={item[0] === selected}><div class="item_text">{item[1]}</div></div>
                    </li>
                </Link>
            </div>
        {/each}
    </ul>
</nav>



 <style>
    .item_text{
        font-size: min(3.5vw, 18px);
        white-space: nowrap; 
    }
    .tabs{
        margin-bottom: 40px;
    }
    ul{
        display: flex;
        justify-content: center;
        padding: 0;
        list-style-type: none;
    }
    li{
        font-size: 18px;
        color: black;
        cursor: pointer;
    }
    .active_inside{
        color: #ff3e00;
        
    }
    .active{
        margin: 0 16px;
        box-sizing: border-box;
        border-bottom: 2px solid #ff3e00;
        padding-bottom: 8px;
        transition: transform;

        
    }
    .inactive{
        margin: 0 16px;
    }
</style>