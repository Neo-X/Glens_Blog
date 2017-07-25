
---
Title: Unreal IndiGolog Bot Project
Date: 2014-05-20 10:20
Modified: Sunday, 21. March 2017 02:06PM 
Category: Publication
Tags: Multi-Agent Simulation, Planning, UnrealEngine, IndiGolog
Author: Glen B
---

This is my project on developing strategic Unreal Tournament bots in the Unreal Development Kit. They were designed to display team work, using well defined team roles. These roles established seniority in a sense where some bot on the team could influence others and with one bot taking command of the teams strategy. The project is focused around the Capture The Flag (CTF) game type in Unreal Tournament. 

Below are videos of gameplay recorded for the project to demonstrate some simple uses of strategy and functionality. In the movies there are two teams fighting against each other to win a CTF game. The blue team members are the new strategic bot focused on in this project and the red team is made up of UTBots designed for the Unreal Tournament game.

<article>
	The Blue Team <br>
	<ul>
	
		<li>Flag Capturer Role (Capturer)</li>
		<p>
		This role is used to describe the member of the team that is the primary flag capturer. The goal
		of this role is to infiltrate the enemies base and steel the flag and return to the home base with the
		flag. This role will differentiate from others because there is far less focus on attacking other
		players. If the capturer does not have the flag then it should try to draw the least amount of attention
		to itself while getting as close to the enemies' flag as possible. When the capturer does have the flag
		it should not turn around and travel backwards to attack because it will travel slower, draw attention
		to itself and navigating backwards perfectly is not realistic.
		</p>
		<li> Capturer Support Role (Capsup)</li>
		<p>
		As the name indicates this role is for defending the Entity that is in the Capturer role. This is
		not a desired role for any Entity that wishes to have longevity. It must do everything it can to
		increase the chances of the Capturer's success. Trying to distract the enemy players from the
		Capturer, destroying as many enemy players that it can and occasionally using its body to block
		incoming fire. A final strategy of the Capsup could be to sacrifice the Capturer only in special cases
		that look very advantageous. If the Capsup can use the Capturer as bait to destroy many of the
		enemy players then it can, keeping in mind that if an enemy touches the flag after the Capturer drops
		it the flag will be returned to the enemy base and progress will be lost.
		</p>
		<li> Base Defender (Defender)</li>
		<p>
		The goal of this role is to prevent the enemy from ever touching its' teams flag. This role can
		also help defend the capturer only when the capturer reaches a close enough distance to the home
		base.
		</p>
		
		<li> Long Range Defender/ Diversion and team leader (LRD)</li>
		<p>
		This role has two main goals. The first is to distract enemy players by attacking them from long
		distances to the best of its ability to draw enemy players away from there base to allow the capturer
		to sneak in and take the flag without resistance. The second role is to act as a long-range defender of
		the base and long-range defender of the capturer. This Entity will search for a long-range weapon
		and then find a vantage point to cover the Capturer and Capsup from a distance. At this vantage
		point the Entity should be able to see a larger percentage of the map giving it more knowledge then
		any other team member.
		This role is also going to function as team leader. This team leader has the ability to change the
		tactics that other team members are currently using. For example the team leader should have the
		best view of the playing field and can inform the Capturer of enemies around the Capturer that the
		Capturer can't see our would have to expose itself to see. If the team leader sees a threat to the
		capturer it will tell the capturer to avoid that threat and if the Capturer has support it will tell the
		Capsup to attack the threat to protect the Capturer.
		</p>
	</ul>
	<p>
		<a href="presentations/IndiGologBots/IndiGologBotTeam.html">Here</a> you can find a presenation on the project.
	</p>
	<p>
		<a href="https://github.com/FracturedPlane/UnrealEnvironmentInterface">Here</a> you can find The code that was used for this project.
	</p>
</article>
<article>
	<table >
		<tr>
			<td>
				<article>
					<p>
						This movie demonstrates the successful use of a diversion strategy used by the blue 
						team.
					</p>
					<video controls poster="images/FirstFrameDiversion.png" width="720" height="410">
					  <source type="video/webm" src="movies/Diversion Strategy.webm"></source>
					  <source type="video/mp4" src="movies/Diversion Strategy.mp4"></source>
					  <source type="video/ogv" src="movies/Diversion Strategy.ogv"></source>
					</video>
				</article>
			</td>
		</tr>
		<tr>
			<td class="mainBody">
				<article>
					<p>
						This video demonstrates the successful execution of the fast attack strategy.
					</p>
					<video controls poster="images/FirstFrameFastAttack.png" width="720" height="410">
					  <source type="video/mp4" src="movies/Fast Attack Strategy.mp4"></source>
					  <source type="video/webm" src="movies/Fast Attack Strategy.webm"></source>
					  <source type="video/ogv" src="movies/Fast Attack Strategy.ogv"></source>
					</video>
				</article>
			</td>
		</tr>
		<tr>
			<td class="mainBody">
				<article>
					<p>
						This is a video recorded near the end of my project to demonstrate a
						longer amount of gameplay.
					</p>
					<video controls poster="images/FirstFrame3on4.png" width="720" height="410">
					  <source type="video/mp4" src="../movies/sampleDemo2-4.mp4"></source>
					  <source type="video/webm" src="../movies/sampleDemo2-4.webm"></source>
					</video>
				</article>
			</td>
		</tr>
	</table>
</article>
## Files

[Bibtex](../files/bibtex/EnvironmentOpt.bib)
[Paper](../projects/EnvironmentOpt/ArchOpt.pdf)
[Presentation](../projects/GameLevelOptimization/paper_errata.pdf)
[comment]: <> ( [Code](https://github.com/FracturedPlane/EnvironmentInterface))

