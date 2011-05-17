<%inherit file="base.mako" />
        <h3>Savaged-Zen(MOD)</h3>
        <table>
            <tr>
                <th width="250">Type</th>
                <th>Total</th>
            </tr>
            <tr>
                <td>OverallInstalls</td>
                <td>${total_kang + total_nonkang|number}</td>
            </tr>
            <tr>
                <td>Last 24 Hours</td>
                <td>${total_last_day|number}</td>
            </tr>
        </table>
        
        <h3>Installs by Version</h3>
        <table>
            <tr>
                <th width="250">Version</th>
                <th>Total</th>
            </tr>
            % for version in version_count:
            <tr><td>${version[1]|h}</td><td>${version[0]|number}</td></tr>
            % endfor
        </table>

        <h3>Installs by Version</h3>
        <table>
            <tr>
                <th width="250">Version</th>
                <th>Total</th>
            </tr>
            % for device in device_count:
            <tr><td>${device[1]|h}</td><td>${device[0]|number}</td></tr>
            % endfor
        </table>

        <h3>Installs by Device</h3>
        <table>
            <tr>
                <th width="250">Device</th>
                <th>Total</th>
            </tr>
            % for device in device_count:
            <tr><td>${device[1]|h}</td><td>${device[0]|number}</td></tr>
            % endfor
        </table>
