# PyDiscord | DataClasses > Guilds






#Imports
from PyDiscord.Functions.Conversions import stringToInteger, stringToBool, detectNone
from PyDiscord.Functions.Dates import creationDateUTC, creationDateLocal

from PyDiscord.DataClasses.Roles import Role
from PyDiscord.DataClasses.Emojis import Emoji
from PyDiscord.DataClasses.Stickers import Sticker





#Classes
class Guild:
    def __init__(self, information: dict):
        self.name = information.get('name')
        self.id = int(information.get('id'))
        self.description = information.get('description')
        self.homeHeader = information.get('home_header')
        self.splashLocal = information.get('splash')
        self.splashDiscovery = information.get('splash_discovery')
        self.Features = information.get('features')
        self.ownerId = int(information.get('owner_id'))
        self.applicationId = stringToInteger(information.get('application_id'))
        self.region = information.get('region')
        self.afkChannelId = stringToInteger(information.get('afk_channel_id'))
        self.afkTimeoutTime = stringToInteger(information.get('afk_timeout'))
        self.systemChannelId = stringToInteger(information.get('system_channel_id'))
        self.systemChannelFlags = stringToInteger(information.get('system_channel_flags'))
        self.widgetEnabled = stringToBool(information.get('widget_enabled'))
        self.widgetChannelId = stringToInteger(information.get('widget_channel_id'))
        self.verificationLevel = stringToInteger(information.get('verification_level'))
        self.Roles = [Role(role, self.id) for role in information.get('roles')]
        self.defaultMessageNotifications = stringToInteger(information.get('default_message_notifications'))
        self.mfaLevel = stringToInteger(information.get('mfa_level'))
        self.explicitContentFilterLevel = stringToInteger(information.get('explicit_content_filter'))
        self.maxPresences = stringToInteger(information.get('max_presences'))
        self.maxMembers = stringToInteger(information.get('max_members'))
        self.maxVideoChannelUsers = stringToInteger(information.get('max_video_channel_users'))
        self.maxVideoStageChannelUsers = stringToInteger(information.get('max_stage_video_channel_users'))
        self.vanityUrl = information.get('vanity_url_code')
        self.premiumTier = int(information.get('premium_tier'))
        self.premiumSubscribers = stringToInteger(information.get('premium_subscriber_count'))
        self.preferredLanguage = information.get('preferred_locale')
        self.rulesChannelId = stringToInteger(information.get('rules_channel_id'))
        self.safetyAlertsChannelId = stringToInteger(information.get('safety_alerts_channel_id'))
        self.publicUpdatesChannelId = stringToInteger(information.get('public_updates_channel_id'))
        self.hubType = information.get('hub_type')
        self.premiumProgressBarEnabled = stringToBool(information.get('premium_progress_bar_enabled'))
        self.latestOnboardingQuestionId = stringToInteger(information.get('latest_onboarding_question_id'))
        self.nswfEnabled = stringToBool(information.get('nsfw'))
        self.nsfwLevel = stringToInteger(information.get('nsfw_level'))
        self.Emojis = [Emoji(emoji) for emoji in information.get('emojis')]
        self.Stickers = [Sticker(sticker) for sticker in information.get('stickers')]
        self.incidentsData = information.get('incidents_data')
        self.embedEnabled = stringToBool(information.get('embed_enabled'))
        self.embedChannelId = stringToInteger(information.get('embed_channel_id'))

        if 'ANIMATED_BANNER' in self.Features: self.bannerAnimated = 'https://cdn.discordapp.com/banners/' + str(self.id) + '/' + information.get('banner') + '.gif'
        else: self.bannerAnimated = None

        if detectNone(information.get('icon')): self.icon = None
        else: self.icon = 'https://cdn.discordapp.com/icons/' + str(self.id) + '/' + information.get('icon') + '.png'

        if detectNone(information.get('banner')): self.banner = None
        else: self.banner = 'https://cdn.discordapp.com/banners/' + str(self.id) + '/' + information.get('banner') + '.png'
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)



    def listInformation(self) -> list:
        return self.__dict__
    


    def __repr__(self):
        return f"{self.name} ({self.id})"




class GuildLimited:
    def __init__(self, information: dict):
        self.name = information.get('name')
        self.id = int(information.get('id'))
        self.Features = information.get('features')
        self.ownerId = int(information.get('owner_id'))
        self.region = information.get('region')
        self.vanityUrl = information.get('vanity_url_code')
        self.premiumTier = int(information.get('premium_tier'))
        self.preferredLanguage = information.get('preferred_locale')
        
        if detectNone(information.get('icon')): self.icon = None
        else: self.icon = 'https://cdn.discordapp.com/icons/' + str(self.id) + '/' + information.get('icon') + '.png'

        if detectNone(information.get('banner')): self.banner = None
        else: self.banner = 'https://cdn.discordapp.com/banners/' + str(self.id) + '/' + information.get('banner') + '.png'

        if 'ANIMATED_BANNER' in self.Features: self.bannerAnimated: str = 'https://cdn.discordapp.com/banners/' + str(self.id) + '/' + information.get('banner') + '.gif'
        else: self.bannerAnimated = None
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)



    def listInformation(self) -> list:
        return self.__dict__
    


    def __repr__(self):
        return f"{self.name} ({self.id})"




class GuildSuperLimited:
    def __init__(self, information: dict):
        self.name = information.get('name')
        self.id = stringToInteger(information.get('id'))
        
        if detectNone(information.get('icon')): self.icon = None
        else: self.icon = 'https://cdn.discordapp.com/icons/' + str(self.id) + '/' + information.get('icon') + '.png'
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)



    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self):
        return f"{self.name} ({self.id})"