### Postmortem: Apache 500 Internal Server Error Outage

#### Issue Summary
**Duration**: June 5, 2024, 09:00 AM - 10:30 AM (UTC)

**Impact**: The Apache web server on our main production server was returning a "500 Internal Server Error," causing a complete service outage. Users were unable to access the website, resulting in a 100% service disruption. Approximately 10,000 users were affected.

**Root Cause**: A typo in the `wp-settings.php` file where "phpp" was mistakenly written instead of "php."

---

#### Timeline

- **09:00 AM** - Issue detected by automated monitoring alert indicating an increase in 500 status codes.
- **09:05 AM** - Incident confirmed by an engineer through manual `curl` requests.
- **09:10 AM** - Investigation began with `strace` attached to the Apache process to diagnose the issue.
- **09:30 AM** - Identified file `/var/www/html/wp-settings.php` as potentially problematic due to a suspected typo.
- **09:40 AM** - Misleading paths: initially suspected a configuration issue with the Apache or PHP installation.
- **09:50 AM** - Issue escalated to the web development team for further inspection.
- **10:00 AM** - Root cause identified as a typo in the `wp-settings.php` file.
- **10:10 AM** - Applied a fix using Puppet to automate the correction of the typo.
- **10:20 AM** - Confirmed resolution by running `curl` requests and checking the server response.
- **10:30 AM** - Service restored and incident closed.

---

#### Root Cause and Resolution
The root cause was a typo in the `wp-settings.php` file where "phpp" was mistakenly written instead of "php." This caused the PHP interpreter to fail, resulting in Apache returning a 500 error.

**Detailed Fix**:
1. Used `strace` to trace system calls and signals of the Apache process, revealing a fatal error when including the `wp-settings.php` file.
2. Verified the error by inspecting the `wp-settings.php` file and found the typo.
3. Created a Puppet script to automate the correction of the typo:
   ```puppet
   file { '/var/www/html/wp-settings.php':
     ensure  => file,
     content => template('my_module/wp-settings.php.erb'),
   }

   exec { 'replace_line':
     command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
     path    => ['/bin', '/usr/bin'],
   }
   ```

   Applied the Puppet script to fix the typo and ensure the correct configuration is maintained.

4. Restarted Apache to apply the changes.

---

#### Corrective and Preventative Measures
To prevent similar issues in the future, the following measures will be implemented:

**Improvements**:
- Implement automated syntax checking for critical configuration files and scripts.
- Enhance monitoring to include checks for PHP errors and failed include statements.

**Tasks**:
1. **Patch Apache Server**: Ensure the server is up to date with the latest security and bug fixes.
2. **Add Monitoring**: 
   - Add file integrity monitoring on critical PHP files.
   - Implement error log monitoring to detect and alert on PHP errors.
3. **Automate Tests**:
   - Develop automated tests to validate configuration files before deployment.
   - Integrate these tests into the CI/CD pipeline.
4. **Documentation**:
   - Update documentation on the configuration and deployment processes.
   - Provide guidelines for error resolution and debugging best practices.

By addressing these areas, we aim to enhance the reliability and stability of our web services, reducing the likelihood of similar issues occurring in the future.