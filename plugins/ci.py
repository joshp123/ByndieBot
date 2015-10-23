from datetime import datetime

import jenkins
from will import settings
from will.plugin import WillPlugin
from will.decorators import respond_to

class ContinuousIntegration(WillPlugin):
    jenkins = None
    def ensure_jenkins(self):
        if not self.jenkins:
            self.jenkins = jenkins.Jenkins(settings.JENKINS_URL,
                                           username=settings.JENKINS_USERNAME,
                                           password=settings.JENKINS_PASSWORD)

        return self.jenkins

    @respond_to("Jeeves status (?P<job_name>.*)")
    def ci_status(self,
                  message,
                  job_name='bynder'):
        """ContinuousIntegration: I can tell you Jenkins CI status
                Usage: "@ByndieBot CI status <job_name>
        """
        print("in ci_status, settings: {}".format(settings))
        server = self.ensure_jenkins()
        try:
            last_build = server.get_job_info(job_name)['builds'][0]
        except IndexError:
            self.reply(message, "No builds for {}".format(job_name))
        except jenkins.NotFoundException:
            self.reply(message, "Can't send find job {}".format(job_name))
            return

        build_info = server.get_build_info(job_name,
                                           last_build['number'])
        build_name = build_info['fullDisplayName']
        build_time = datetime.fromtimestamp(build_info['timestamp'] / 1000)
        build_status = build_info['result']
        if build_status == 'SUCCESS':
            self.reply(message, "Jeeves finished {} at {}"
                                .format(build_name, build_time))
        elif build_status == 'FAILURE':
            self.reply(message, "Build {} FAILED at {}"
                                .format(build_name, build_time))
        elif not build_status:  # == In progress
            self.reply(message, "Don't disturb Jeeves, he's still busy with {}"
                                .format(build_status))
        else:
            self.reply(message, "Unknown status for {}".format(build_name))
