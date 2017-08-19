from unittest import TestCase
from extractor.process import Process

from unittest.mock import Mock


class ProcessTest(TestCase):


    pass



    def test_run__when__new_records_are_created__should__process_them_by_sale_data_processor(self):
        """
        Given: file reader return new records
        When: run()
        Then: sale_data_processor is executed passing the new records
        """

        records = [5, 6, 7] # should not be empty, new_records will not be populated

        csv_file = "csv file"
        file_reader = Mock()
        sale_raw_data_repository = Mock()
        sale_data_processor = Mock()

        file_reader.read = Mock(return_value=records)
        sale_raw_data_repository.save = Mock(side_effect=lambda x: x)


        process_ = Process(file_reader, sale_raw_data_repository, sale_data_processor)

        # act
        process_.run(csv_file)


        # assert
        sale_data_processor.process_new_records.assert_called_with(records)
