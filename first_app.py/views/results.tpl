<!DOCTYPE html>
<html>
    <head>
        <title>Project Company - {{ title }}</title>
    </head>

    <body>
        <header>
            <p><a href="/">Return to Home Page</a></p>
        </header>

        <h1>{{ title }}</h1>

        % if len(records) < 1:
        <p><strong>No records found.</strong></p>
        % else:
        <table>
            <tr>
                % for field in records[0].keys():
                <th>{{ field }}</th>
                % end
            </tr>
            % for record in records:
            <tr>
                % for field in record:
                <td>{{ field }}</td>
                % end
            </tr>
            % end
        </table>
        % end

        <footer>
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>
