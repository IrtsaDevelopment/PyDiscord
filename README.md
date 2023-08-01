# PyDiscord
The [**Discord API**](https://discord.com/developers/docs/reference) made for normal users put into [**python**](https://www.python.org).
<br />
<br />
<br />
<br />

## Import Notice
**Discord** frowns on what is called "self-bots" (please see [here](https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots-)):
> Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is forbidden, and can result in an account termination if found.

Instead, Discord does have support for what are "bots" (please see [here](https://discord.com/developers/docs/reference)):
> Discord's API provides a separate type of user account dedicated to automation, called a bot account. Bot accounts can be created through the applications page, and are authenticated using a token (rather than a username and password)
<br />
<br />

As such, this has intentionally left out certain endpoints of the API so that you may only retrieve information from your own account. To access the information, you will need to authenticate using an **email** and **password**, along with **2FA** if applicable to your account. 
<br />

If you wish to write a Discord bot in python, a good source can be found [**here**](https://github.com/Rapptz/discord.py) *(you should check it out)*.
<br />
<br />

While I cannot deny the possibility that one can figure out or read up on the other endpoints as well in order to utilize them, I would personally advise against strong usage of them to avoid possible account termination.
<br />
<br />
<br />

Kindly, I ask to respect this and do not utilize for malicious intent.
<br />
<br />
<br />
<br />
<br />
<br />

## Installation
With `git` [GitHub](https://github.com/IrtsaDevelopment/PyDiscord):
```
git clone https://github.com/IrtsaDevelopment/PyDiscord.git
```
<br />
<br />
<br />
<br />
<br />
<br />

## Usage
To import, you may use:
```py
from PyDiscord.Client import Discord
```
<br />

Afterwhich, you would need to login (and verify if needed).
```py
client = Discord()

client.login('account@testing.com', 'password')
# Login to discord.

client.verify(123456)
# Verifies if needed.
# You can utilize client.needAuthentication to check if this is required.
# Currently does not support backup codes from discord, only utilizing totp.
```
<br />

After login (and verification if needed), the following can be used:
```py
client.getGuild(637283625251738321)
# Gets a guild given the ID.
# The current user must be a part of the guild.
# Returns Guild objects.

client.getCurrentGuilds()
# Gets a list of guilds the user is in.
# Returns a list of GuildSuperLimited objects.

client.getUser(123242428284345329)
# Gets a user given the ID.
# What gets returned depends on if you are friends with said person or share a guild.
# Will return your current user information if no ID is provided.

client.getFriends()
# Gets a list of users the current user is friends with.
# Returns a list of UserFriend objects.

client.getMessages(134253256372563345, limit = 50)
# Gets a list of messages from the given channel ID.
# The number of messages returned can be limited with the "limit" parameter which defaults to 50.
# Returns a list of Message objects.
```
