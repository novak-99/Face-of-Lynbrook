<script>
	import {state, genImgFile} from "../../stores/store.js"
	import { ToastContainer, toast } from "svelte-toastify";
	$state = "/submit"

	let fileInput;

	toast.configure({
    	position: toast.POSITION.TOP_RIGHT
	});

	// Upload file wrt backend
	let rand = -1; 
	const uploadFile =(e)=>{
  		let image = e.target.files[0];
        let reader = new FileReader();
		const formData = new FormData();
        reader.readAsDataURL(image);
		
		formData.append(
			"image",
			image
      	);

		fetch('./saveUpload', {
            method: 'POST',
            body: formData,
        })
		.then(d => d.text())
		.then(d => toastUser(JSON.parse(d).success, JSON.parse(d).err_id))

		

	}
	function toastUser(success, err_id){
			const ERR_CODES = {
				"ERR0":"Could not upload image: An unknown error occured",
				"ERR1":"Could not upload image: The image uploaded was not a face",
				"ERR2":"Could not upload image: Caught an unknown exception"
			}
			const SUCCESS = "Face image uploaded successfully"
			if(success) toast.success(SUCCESS)
			else toast.error(ERR_CODES[err_id])
		}
</script>
<center>
<h1>Submit Data</h1>

<p>
The Face of Lynbrook, like any other machine learning model, requires data, and here, that means
you- the Lynbrook student! To do so, follow the steps below to upload an image. 
</p>

<h2>Step 1</h2>
<p>
Orient yourself correctly. Ensure that your face is fully within frame and that it takes up most of the image. It should look like the example below: 
</p>


<img class="example-upload" src="imgs/submit/example-upload.png" alt="example-upload" width="200" height="200"/>

<h2>Step 2</h2>
<p>
Submit your face image! Ensure that it is an accepted file type (.jpg, .jpeg or .png).
</p>



<a href="javascript:void(0)">
<img on:click={()=>{fileInput.click()}} src="imgs/submit/upload-image-icon.png" alt="Upload an img" width=128 height=128/>
<input style="display:none" onclick={"this.value=null;"} type="file" accept=".jpg, .jpeg, .png" on:change={(e)=>uploadFile(e)} bind:this={fileInput} >
</a>

	<div class="upload-text">
	<b>Upload an Image</b>
	<br>
	</div>

</center>

<ToastContainer />

<style>
	.upload-text{
		margin-top: 10px;
	}
	h2{
		width: fit-content;
		margin-top: 30px;
		border-bottom: 1px solid #ff3e00;
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 2em;
		font-weight: 100;
		outline: none;

	}
	p{
		/* font-size: 1em;*/
		font-weight: 200;  
		text-align: left;
		word-wrap: break-word;
		max-width: 600px;
	}

	img{
		transition: transform .2s;
		margin-top: 15px;
	}

	.example-upload{
		border: 2px solid black;
	}

	img:hover {
		transform: scale(1.2); 
	}
</style>