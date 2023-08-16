# SpiderFoot BigIP Cookie Decoder Plugin

This SpiderFoot plugin is designed to decode BigIP cookies from HTTP headers and extract IP addresses and ports.

## Installation

1. Clone or download this repository to your local machine.

2. Navigate to the module directory:

   ```shell
   cd BigIP_Cookie_Decoder_SpiderFoot
   ```

3. Move the module folder to the SpiderFoot modules directory. Assuming SpiderFoot is installed in `/usr/share/spiderfoot`, use the following command:

   ```shell
   sudo mv sfp_bigip_cookie_decoder /usr/share/spiderfoot/modules/
   ```

## Usage

1. Start SpiderFoot:

   ```shell
   spiderfoot -l 127.0.0.1:5001
   ```

2. Open SpiderFoot in your web browser and log in.

3. Navigate to "Configuration" and select "Manage Modules."

4. Locate the "BigIP Cookie Decoder" module and click "Enable."

5. Return to the main SpiderFoot interface and start an assessment.

6. The module will automatically process HTTP headers for BigIP cookies and attempt to decode them.

## Configuration

The module provides an option to configure the prefix of the cookie string to check for. The default prefix is "BigIP."

To configure this option:

1. Navigate to "Configuration" in SpiderFoot.

2. Locate the "BigIP Cookie Decoder" module and click "Configure."

3. Update the "Cookie Prefix" option as needed.

4. Click "Save Changes."

## Author

- Author: vpanal

## License

This module is licensed under the GNU General Public License (GPL).

For more information about SpiderFoot, visit [SpiderFoot's GitHub Repository](https://github.com/smicallef/spiderfoot).

For more information about SpiderFoot modules, refer to the [SpiderFoot Documentation](https://github.com/smicallef/spiderfoot/wiki/Module-Development).
