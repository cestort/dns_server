from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
hosts_file_path = os.path.join(
    os.path.dirname(__file__), 'data', 'dnsmasq.hosts')


def read_hosts():
    if not os.path.exists(hosts_file_path):
        return []
    with open(hosts_file_path, 'r') as file:
        lines = file.readlines()
    records = [line.strip().split() for line in lines if line.strip()]
    return records


def write_hosts(records):
    with open(hosts_file_path, 'w') as file:
        for record in records:
            file.write(f"{record[0]} {record[1]}\n")


@app.route('/')
def index():
    records = read_hosts()
    return render_template('index.html', records=records)


@app.route('/add', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        domain_name = request.form['domain_name']
        records = read_hosts()
        records.append([ip_address, domain_name])
        write_hosts(records)
        os.system('sudo systemctl restart dnsmasq')
        return redirect(url_for('index'))
    return render_template('add_record.html')


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete_record(record_id):
    records = read_hosts()
    if 0 <= record_id < len(records):
        records.pop(record_id)
        write_hosts(records)
        os.system('sudo systemctl restart dnsmasq')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
