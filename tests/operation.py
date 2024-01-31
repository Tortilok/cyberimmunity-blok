import os
import sys
import random
import unittest


__location__: str = os.path.dirname(os.path.abspath(__file__))
monitor_path: str = os.path.join(__location__,
                                 os.pardir,
                                 'train', 'modules', 'monitor', 'module')

if not os.path.exists:
    print('failed to find policies in', monitor_path)
    exit(1)
else:
    sys.path.insert(1, monitor_path)
    from policies import policies, check_operation


length: int = len(policies)
event_id: int = 0


def next_event(self) -> int:
    global event_id

    event_id += 1
    return event_id


class TestOperation(unittest.TestCase):
    event = next_event

    def test_true(self):
        result = check_operation(self.event(), {
            'source': policies[1]['src'],
            'deliver_to': policies[1]['dst']
        })

        self.assertEqual(result, True)

    def test_false(self):
        result = check_operation(self.event(), {
            'source': 'foo',
            'deliver_to': 'bar'
        })

        self.assertEqual(result, False)

    def test_true2(self):
        result = check_operation(self.event(), {
            'source': policies[2]['src'],
            'deliver_to': policies[2]['dst']
        })

        self.assertEqual(result, True)

    def test_blank(self):
        result = check_operation(self.event(), {
            'source': '',
            'deliver_to': ''
        })

        self.assertEqual(result, False)

    def test_con(self):
        ops = (
            ('con', 'chipher', True),
            ('chipher', 'con', True),
            ('con', 'can', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_can(self):
        ops = (
            ('can', 'con', False),
            ('chipher', 'can', True),
            ('can', 'chipher', True),
            ('iy', 'can', True),
            ('can', 'bvi', False)
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_trustCan(self):
        ops = (
            ('trustCan', 'con', False),
            ('chipher', 'trustCan', True),
            ('trustCan', 'chipher', False),
            ('iy', 'trustCan', False),
            ('trustCan', 'bvi', False),
            ('trustCan', 'rpdp', True),
            ('trustCan', 'saytp', True),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_chipher(self):
        ops = (
            ('chipher', 'trustCan', True),
            ('chipher', 'con', True),
            ('chipher', 'rpdp', False),
            ('chipher', 'can', True),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_tskbm(self):
        ops = (
            ('tskbm', 'can', True),
            ('tskbm', 'con', False),
            ('tskbm', 'pir', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_pri(self):
        ops = (
            ('can', 'pri', True),
            ('pri', 'can', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_bi(self):
        ops = (
            ('can', 'bi', True),
            ('bi', 'trustCan', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_iy(self):
        ops = (
            ('iy', 'can', True),
            ('trustCan', 'iy', True),
            ('iy', 'trustCan', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_saytp(self):
        ops = (
            ('saytp', 'can', True),
            ('trustCan', 'saytp', True),
            ('saytp', 'trustCan', False),
            ('can', 'saytp', False),
            ('saytp', 'tskbm', False)
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_rpdp(self):
        ops = (
            ('rpdp', 'can', True),
            ('trustCan', 'rpdp', True),
            ('rpdp', 'trustCan', False),
            ('can', 'rpdp', False),
            ('rpdp', 'rpdp', False)
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_bvi(self):
        ops = (
            ('bvi', 'trustCan', True),
            ('bvi', 'can', False),
            ('bvi', 'chipher', False),
            ('bvi', 'iy', False)
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_pir(self):
        ops = (
            ('pir', 'trustCan', True),
            ('pir', 'tskbm', False),
            ('pir', 'con', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_oskp(self):
        ops = (
            ('oskp', 'trustCan', True),
            ('oskp', 'iy', False),
            ('oskp', 'tskbm', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])

    def test_self(self):
        ops = (
            ('oskp', 'oskp', False),
            ('chipher', 'chipher', False),
            ('rpdp', 'rpdp', False),
        )

        for op in ops:
            result = check_operation(self.event(), {
                'source': op[0],
                'deliver_to': op[1]
            })

            self.assertEqual(result, op[2])


if __name__ == '__main__':
    unittest.main(verbosity=2)
