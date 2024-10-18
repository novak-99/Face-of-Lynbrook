<script>
	import {state} from "../../stores/store.js"
	$state = "/behindthescenes"

	let imgWidth = 130
	let imgHeight = 173.3
</script>

<center>
<div class="text-column">
	<h1>Behind the Scenes</h1>

	<p>
		The Face of Lynbrook is a machine learning application that makes novel generations from the faces of the 
		Lynbrook student body. 
	</p>

	<p>
		Various techniques have been used in ethnology to explore the many diverse phenotypes of humans, 
		though most are rudimentary in nature. The most popular of these is the facial averaging technique. 
		It creates generalizations of people groups by taking the arithmetic mean (average) of a large sample of 
		face images in the same pose. 
	</p>

	<p>
		The examples below illustrate this technique. The first three images represent facial averaging of 
		the people groups native to the European Balkans, Brazillian Amazon, and Northern India. The fourth 
		image illustrates facial averaging on 1,000 generated images of miscellaneous faces. 
	</p>
	<div class="img_avg">
	<img class="averages" src="imgs/behindthescenes/dinaridm.jpg" alt="balkan" width={imgWidth} height={imgHeight}/>
	<img class="averages" src="imgs/behindthescenes/amazonidm.jpg" alt="amazon" width={imgWidth} height={imgHeight} />
	<img class="averages" src="imgs/behindthescenes/indidm.jpg" alt="india" width={imgWidth} height={imgHeight} />
	<img class="averages" src="imgs/behindthescenes/1kavg.png" alt="imgavg" width={imgWidth} height={imgHeight} />
	</div>
	<p>
		While the results may look promising, the issue lies in the algorithm's simplicity. 
		This leads both to outlier sensitivity as well as an inability to generate novel generalizations.
		Generative Adversarial Networks (GANs) are a more sophisticated technique that are able to generate 
		approximations of the inputs. 
	</p>

	<p>
		This application presents three points of interest. First, in contrast to earlier and older methods of analyzing 
		populations, the Face of Lynbrook uses the generative models mentioned above. Most previous population analysis has used 
		techniques such as the previously mentioned averaging technique. The Face of Lynbrook utilizes the generative 
		StyleGAN2-ADA model, created by NVIDIA. 
	</p>
	<p>
		Second, it analyzes populations that are heterogenous in nature. Whereas the previous three population analysis examples
		above were all dealing with homogenous populations from specific areas, the Lynbrook population is heterogenous. 
		That is to say that each individual is not the same- the population is diverse. 
	</p>
	<p>
		Finally, the model has the problem of working with a constrained input size. Most GAN models require data on the order of 
		10,000, 100,000, or even 1M+. This model, however, is built with an estimated lower bound of N = 50 submissions. Luckily, the model, 
		StyleGAN2-ADA, was specifically built for small datasets. Even then however, a size of 50 was still too small. A training regieme 
		of incremental distribution augmentation- training for a short period of time to alter the nature of the distribution- was highly 
		successful, because the StyleGAN2-ADA model was already excessively pre-trained. 
	</p>
	<p>
		The model can be seen as successful in these respects- heterogenous population, novel generative applications, and 
		small sample size- in the generated results. Here are a few examples showing this success:
	</p>

	<div class="img_group">
		<img src="imgs/tryit/gen1.png" alt="gen1" width="150" height="150"/>
		<img src="imgs/tryit/gen2.png" alt="gen2" width="150" height="150"/>
	</div>
</div>

</center>

<style>

	.img_avg{
		justify-content: right;
		display: block;
	}	

	.img_group{
		justify-content: right;
		display: block;
	}	

	img{
		border: 2px solid black;
		margin:10px;
		transition: transform .2s; 


		/* height: auto;
		width: auto; */
	}

	img:hover {
  		transform: scale(1.2); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
	}

    p{
		/* font-size: 1em;
		font-weight: 200;   */
		font-weight: 200;
		text-align: left;
		word-wrap: break-word;
		max-width: 600px;

    }
</style>
