# POSTMORTEM

## Issue Summary
A pull request which had many bugs was merged with the production branch and hence caused the website to
be temporarily inaccessible. The website was down for a total of 10 minutes during this time, all clients were
not able to use the website as they could not access it.

## Timeline
* 2:04PM GMT - An engineer monitoring the system realized the website was down
* 2:05PM GMT - Investigations were carried out to identify the root cause
* 2:09PM GMT - Root cause was discovered (a merged pull request which was not reviewed)
* 2:13PM GMT - Reverted changes made to the production branch hence restoring normal functionality
* 2:14PM GMT - Verified that the website was up and running again

## Root Cause & Resolution
The root cause for the break in production was a bad pull request which was made by an intern. The pull request
was not reviewd thoroughly and tested before it was merged and hence caused the break in production.

### The fix
To fix this, the team first made sure that the web servers and everything else was configured properly. After the team
confirmed everything was correctly configured, the team now checked the codebases and files to ensure that
everything was okay there too. Thats when the bad pull request that was merged was discovered. The team quickly
reverted all the changes made to the codebase by the merge and then put the website back in production after testing
and making sure everything was working how it was supposed to.

## Corrective & Preventative Measures
* All pull request will go through a rigorous testing before being merged with the main production branch
* All pull request will be reviewed by a team of senior developers before being mereged with the production branch.
* Changes made to codebases will be tested before pull request are made.
