"""
Sims 4 Video Vixen Career Mod
A custom career path for content creators and influencers
"""

from sims4.tuning.tuning_base import HasTunableReference
from sims4.tuning.instances import TunedInstanceMetaclass
from careers.career import Career
from careers.career_level import CareerLevel


class VideoVixenCareer(Career, metaclass=TunedInstanceMetaclass, manager=services.get_instance_manager(sims4.resources.Types.CAREER)):
    """
    Video Vixen Career - A path for Sims who want to become content creators and influencers
    """
    
    INSTANCE_TUNABLES = {
        'career_name': 'Video Vixen',
        'career_description': 'Create viral content and build your audience as a Video Vixen influencer!',
        'max_level': 10,
        'experience_rate': 1.0,
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.career_name = 'Video Vixen'
        self.career_levels = self._create_career_levels()
    
    def _create_career_levels(self):
        """Create the 10 levels of the Video Vixen career"""
        levels = {}
        
        career_progression = [
            {
                'level': 1,
                'title': 'Aspiring Content Creator',
                'salary': 300,
                'tasks': ['Film Videos', 'Edit Content', 'Gain Followers'],
                'skills': ['Video Production'],
            },
            {
                'level': 2,
                'title': 'Up-and-Coming Vlogger',
                'salary': 500,
                'tasks': ['Create Trending Videos', 'Network Online', 'Respond to Comments'],
                'skills': ['Video Production', 'Social Media'],
            },
            {
                'level': 3,
                'title': 'Rising Star',
                'salary': 750,
                'tasks': ['Collaborate with Creators', 'Plan Series', 'Increase Views'],
                'skills': ['Video Production', 'Social Media', 'Charisma'],
            },
            {
                'level': 4,
                'title': 'Viral Sensation',
                'salary': 1200,
                'tasks': ['Go Viral', 'Sponsor Content', 'Expand Audience'],
                'skills': ['Video Production', 'Social Media', 'Charisma'],
            },
            {
                'level': 5,
                'title': 'Internet Celebrity',
                'salary': 1800,
                'tasks': ['Host Live Events', 'Create Branded Content', 'Mentor Newcomers'],
                'skills': ['Video Production', 'Social Media', 'Charisma', 'Cooking'],
            },
            {
                'level': 6,
                'title': 'Media Influencer',
                'salary': 2500,
                'tasks': ['Manage Brand Deals', 'Produce High-Quality Content', 'Lead Team'],
                'skills': ['Video Production', 'Social Media', 'Charisma', 'Business'],
            },
            {
                'level': 7,
                'title': 'Content King/Queen',
                'salary': 3500,
                'tasks': ['Direct Content Team', 'Negotiate Partnerships', 'Create Exclusive Content'],
                'skills': ['Video Production', 'Social Media', 'Charisma', 'Business', 'Comedy'],
            },
            {
                'level': 8,
                'title': 'Entertainment Icon',
                'salary': 4500,
                'tasks': ['Produce Original Series', 'Launch New Platforms', 'Industry Leadership'],
                'skills': ['Video Production', 'Social Media', 'Charisma', 'Business', 'Comedy'],
            },
            {
                'level': 9,
                'title': 'Media Mogul',
                'salary': 5500,
                'tasks': ['Run Production Studio', 'Mentor Industry Talent', 'Create Blockbuster Content'],
                'skills': ['Video Production', 'Social Media', 'Charisma', 'Business', 'Comedy', 'Logic'],
            },
            {
                'level': 10,
                'title': 'Legend of Digital Media',
                'salary': 7000,
                'tasks': ['Define Industry Standards', 'Oversee Empire', 'Inspire Next Generation'],
                'skills': ['Video Production', 'Social Media', 'Charisma', 'Business', 'Comedy', 'Logic'],
            },
        ]
        
        for level_data in career_progression:
            level = CareerLevel(
                level=level_data['level'],
                title=level_data['title'],
                salary=level_data['salary'],
                tasks=level_data['tasks'],
                required_skills=level_data['skills'],
            )
            levels[level_data['level']] = level
        
        return levels
    
    def get_career_level(self, level):
        """Get a specific career level"""
        return self.career_levels.get(level)
    
    def get_all_levels(self):
        """Get all career levels"""
        return list(self.career_levels.values())


# Career-specific tasks
class VideoVixenTasks:
    """Daily tasks for Video Vixen career"""
    
    TASKS = {
        'film_videos': {
            'name': 'Film Videos',
            'description': 'Create new video content',
            'experience_gain': 25,
            'time_required': 3,
        },
        'edit_content': {
            'name': 'Edit Content',
            'description': 'Edit and polish your videos',
            'experience_gain': 20,
            'time_required': 2,
        },
        'gain_followers': {
            'name': 'Gain Followers',
            'description': 'Promote your content online',
            'experience_gain': 15,
            'time_required': 2,
        },
        'collaborate': {
            'name': 'Collaborate with Creators',
            'description': 'Partner with other content creators',
            'experience_gain': 35,
            'time_required': 4,
        },
        'go_viral': {
            'name': 'Go Viral',
            'description': 'Create content that goes viral',
            'experience_gain': 50,
            'time_required': 5,
        },
    }
    
    @classmethod
    def get_task(cls, task_id):
        """Get a specific task"""
        return cls.TASKS.get(task_id)
    
    @classmethod
    def get_all_tasks(cls):
        """Get all available tasks"""
        return list(cls.TASKS.values())
